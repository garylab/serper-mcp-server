# Time MCP Server

A Model Context Protocol server that provides **Google Search via Serper**. This server enables LLMs to get search result information from Google.

## Available Tools

- `google_search` - Get the result of the search.
  - Required arguments:
    - `q` (string): The query to search for
  - Optional arguments:
    - `gl` (string): The country to search in, e.g. us, uk, ca, au, etc.
    - `location` (string): The location to search in, e.g. San Francisco, CA, USA
    - `hl` (string): The language to search in, e.g. en, es, fr, de, etc.
    - `tbs` (string): The time period to search in, e.g. d, w, m, y
    - `num` (integer): The number of results to return, max is 100 (default: 10)
    - `page` (integer): The page number to return, first page is 1 (default: 1)


## Installation

### Using `uv` (recommended)

When using [`uv`](https://docs.astral.sh/uv/) no specific installation is needed. We will
use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run *serper-mcp-server*.

### Using `pip`

Alternatively you can install `serper-mcp-server` via pip:

```bash
pip install serper-mcp-server
```

After installation, you can run it as a script using:

```bash
python -m serper_mcp_server
```

## Configuration

### Configure for Claude.app

Add to your Claude settings in file `claude_desktop_config.json`:

- Using uvx
    ```json
    "mcpServers": {
    "serper": {
        "command": "uvx",
        "args": ["serper-mcp-server"]
    }
    }
    ```
- Using pip installation
    ```json
    "mcpServers": {
    "time": {
        "command": "python",
        "args": ["-m", "serper_mcp_server"]
    }
    }
    ```


## Debugging

You can use the MCP inspector to debug the server. For `uvx` installations:

```bash
npx @modelcontextprotocol/inspector uvx serper-mcp-server
```

Or if you've installed the package in a specific directory or are developing on it:

```bash
cd path/to/servers/src/time
npx @modelcontextprotocol/inspector uv run serper-mcp-server
```

## Examples of Questions for Claude

1. "What time is it now?" (will use system timezone)
2. "What time is it in Tokyo?"
3. "When it's 4 PM in New York, what time is it in London?"
4. "Convert 9:30 AM Tokyo time to New York time"


## License

serper-mcp-server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.