# Serper MCP Server
[![smithery badge](https://smithery.ai/badge/@garylab/serper-mcp-server)](https://smithery.ai/server/@garylab/serper-mcp-server)

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


## Usage

### Installing via Smithery

To install Serper MCP Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@garylab/serper-mcp-server):

```bash
npx -y @smithery/cli install @garylab/serper-mcp-server --client claude
```

### Using `uv` (recommended)

1. Make sure you had installed [`uv`](https://docs.astral.sh/uv/) on your os system.

2. In your MCP client code configuration or **Claude** settings (file `claude_desktop_config.json`) add `serper` mcp server:
    ```json
    {
        "mcpServers": {
            "serper": {
                "command": "uvx",
                "args": ["serper-mcp-server"],
                "env": {
                    "SERPER_API_KEY": "<Your Serper API key>"
                }
            }
        }
    }
    ```
    `uv` will download mcp server automatically using `uvx` from [pypi.org](https://pypi.org/project/serper-mcp-server/) and apply to your MCP client.

### Using `pip` for project
1. Add `serper-mcp-server` to your MCP client code `requirements.txt` file.
    ```txt
    serper-mcp-server
    ```

2. Install the dependencies.
    ```shell
    pip install -r requirements.txt
    ```

3. Add the configuration for you client:
    ```json
    {
        "mcpServers": {
            "serper": {
                "command": "python3",
                "args": ["-m", "serper_mcp_server"],
                "env": {
                    "SERPER_API_KEY": "<Your Serper API key>"
                }
            }
        }
    }
    ```


### Using `pip` for globally usage

1. Make sure the `pip` or `pip3` is in your os system.
    ```bash
    pip install serper-mcp-server
    # or
    pip3 install serper-mcp-server
    ```

2. MCP client code configuration or **Claude** settings, add `serper` mcp server:
    ```json
    {
        "mcpServers": {
            "serper": {
                "command": "python3",
                "args": ["serper-mcp-server"],
                "env": {
                    "SERPER_API_KEY": "<Your Serper API key>"
                }
            }
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
cd path/to/servers/src/serper
npx @modelcontextprotocol/inspector uv run serper-mcp-server -e SERPER_API_KEY=<the key>
```


## License

serper-mcp-server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.
