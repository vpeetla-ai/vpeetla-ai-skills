#!/usr/bin/env python3
"""Minimal MCP stdio server — read-only org corpus tools (JSON-RPC 2.0).

Usage:
  CORPUS_DIR=./corpus python -m mcp.stdio_server

Compatible with Cursor MCP config:
  {"command": "python", "args": ["-m", "mcp.stdio_server"], "env": {"CORPUS_DIR": "..."}}
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any


PROTOCOL_VERSION = "2024-11-05"
SERVER_NAME = "vpeetla-org-tools"
SERVER_VERSION = "0.1.0"


def _corpus_dir() -> Path:
    return Path(os.getenv("CORPUS_DIR", ".")).resolve()


def _tools() -> list[dict[str, Any]]:
    return [
        {
            "name": "read_file",
            "description": "Read a file from the corpus by relative path (read-only)",
            "inputSchema": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
            },
        },
        {
            "name": "search_docs",
            "description": "Full-text search across markdown corpus (read-only)",
            "inputSchema": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        },
    ]


def _read_file(path: str) -> str:
    root = _corpus_dir()
    target = (root / path).resolve()
    if not str(target).startswith(str(root)):
        return f"Error: path escapes corpus: {path}"
    if not target.is_file():
        return f"Error: file not found: {path}"
    return target.read_text(encoding="utf-8")[:8000]


def _search_docs(query: str) -> str:
    root = _corpus_dir()
    hits: list[str] = []
    terms = [t for t in query.lower().split() if len(t) > 2]
    for md in sorted(root.glob("**/*.md")):
        text = md.read_text(encoding="utf-8")
        if not terms or any(t in text.lower() for t in terms):
            rel = md.relative_to(root)
            hits.append(f"[{rel}] {text[:400]}...")
    return "\n---\n".join(hits[:5]) if hits else "No matches."


def _call_tool(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    if name == "read_file":
        text = _read_file(str(arguments.get("path", "")))
    elif name == "search_docs":
        text = _search_docs(str(arguments.get("query", "")))
    else:
        return {"content": [{"type": "text", "text": f"Unknown tool: {name}"}], "isError": True}
    return {"content": [{"type": "text", "text": text}], "isError": False}


def _respond(msg_id: Any, result: Any) -> None:
    sys.stdout.write(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": result}) + "\n")
    sys.stdout.flush()


def _error(msg_id: Any, code: int, message: str) -> None:
    sys.stdout.write(
        json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": code, "message": message}}) + "\n"
    )
    sys.stdout.flush()


def handle_message(msg: dict[str, Any]) -> None:
    msg_id = msg.get("id")
    method = msg.get("method", "")
    params = msg.get("params") or {}

    if method == "initialize":
        _respond(
            msg_id,
            {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {}},
                "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
            },
        )
        return

    if method == "notifications/initialized":
        return

    if method == "tools/list":
        _respond(msg_id, {"tools": _tools()})
        return

    if method == "tools/call":
        name = str(params.get("name", ""))
        arguments = params.get("arguments") or {}
        _respond(msg_id, _call_tool(name, arguments))
        return

    if msg_id is not None:
        _error(msg_id, -32601, f"Method not found: {method}")


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        if msg.get("jsonrpc") != "2.0":
            continue
        handle_message(msg)


if __name__ == "__main__":
    main()
