"""Tests for MCP stdio server."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "mcp" / "fixtures"


class MCPStdioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        CORPUS.mkdir(parents=True, exist_ok=True)
        (CORPUS / "guide.md").write_text(
            "# Style Guide\n\nLinkedIn posts should be professional.\n",
            encoding="utf-8",
        )

    def _run_exchange(self, request: dict) -> dict:
        env = os.environ.copy()
        env["CORPUS_DIR"] = str(CORPUS)
        proc = subprocess.run(
            [sys.executable, "-m", "mcp.stdio_server"],
            input=json.dumps(request) + "\n",
            capture_output=True,
            text=True,
            cwd=str(ROOT),
            env=env,
            timeout=10,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        lines = [ln for ln in proc.stdout.strip().splitlines() if ln]
        self.assertTrue(lines, "no stdout from server")
        return json.loads(lines[-1])

    def test_tools_list(self) -> None:
        resp = self._run_exchange({"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}})
        self.assertIn("result", resp)
        names = {t["name"] for t in resp["result"]["tools"]}
        self.assertIn("read_file", names)
        self.assertIn("search_docs", names)

    def test_read_file(self) -> None:
        resp = self._run_exchange(
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/call",
                "params": {"name": "read_file", "arguments": {"path": "guide.md"}},
            }
        )
        text = resp["result"]["content"][0]["text"]
        self.assertIn("LinkedIn", text)

    def test_search_docs(self) -> None:
        resp = self._run_exchange(
            {
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {"name": "search_docs", "arguments": {"query": "LinkedIn professional"}},
            }
        )
        text = resp["result"]["content"][0]["text"]
        self.assertIn("guide.md", text)


if __name__ == "__main__":
    unittest.main()
