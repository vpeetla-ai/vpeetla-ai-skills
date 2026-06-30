# MCP stdio server — vpeetla-ai org tools

Read-only corpus tools packaged as a **stdio MCP server** for Cursor and other MCP clients.

## Tools

| Tool | Side effect | Description |
|------|-------------|-------------|
| `read_file` | No | Read file from `CORPUS_DIR` |
| `search_docs` | No | Search markdown in corpus |

## Run locally

```bash
CORPUS_DIR=../loop-engine-agent-platform/corpus python -m mcp.stdio_server
```

## Cursor config (`.cursor/mcp.json`)

```json
{
  "mcpServers": {
    "vpeetla-org-tools": {
      "command": "python3",
      "args": ["-m", "mcp.stdio_server"],
      "cwd": "/path/to/vpeetla-ai-skills",
      "env": {
        "CORPUS_DIR": "/path/to/loop-engine-agent-platform/corpus"
      }
    }
  }
}
```

## Test

```bash
python tests/test_mcp_stdio.py
```

Publish and git tools remain in application services with **AegisAI gateway** — not exposed via this read-only server.
