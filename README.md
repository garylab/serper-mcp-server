# Serper MCP Server
[![smithery badge](https://smithery.ai/badge/@garylab/serper-mcp-server)](https://smithery.ai/server/@garylab/serper-mcp-server)

A Model Context Protocol server that provides **Google Search via Serper**. This server enables LLMs to get search result information from Google.

## Available Tools

- `google_search` - Set [all the parameters](src/serper_mcp_server/schemas.py#L15)
- `google_search_images` - Set [all the parameters](src/serper_mcp_server/schemas.py#L15)
- `google_search_videos` - Set [all the parameters](src/serper_mcp_server/schemas.py#L15)
- `google_search_places` - Set [all the parameters](src/serper_mcp_server/schemas.py#L20)
- `google_search_maps` - Set [all the parameters](src/serper_mcp_server/schemas.py#L24)
- `google_search_reviews` - Set [all the parameters](src/serper_mcp_server/schemas.py#L34)
- `google_search_news` - Set [all the parameters](src/serper_mcp_server/schemas.py#L15)
- `google_search_shopping` - Set [all the parameters](src/serper_mcp_server/schemas.py#L45)
- `google_search_lens` - Set [all the parameters](src/serper_mcp_server/schemas.py#L50)
- `google_search_scholar` - Set [all the parameters](src/serper_mcp_server/schemas.py#L20)
- `google_search_parents` - Set [all the parameters](src/serper_mcp_server/schemas.py#L56)
- `google_search_autocomplete` - Set [all the parameters](src/serper_mcp_server/schemas.py#L20)
- `webpage_scrape` - Set [all the parameters](src/serper_mcp_server/schemas.py#L62)


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
git clone https://github.com/garylab/serper-mcp-server.git
cd serper-mcp-server
npx @modelcontextprotocol/inspector uv run serper-mcp-server -e SERPER_API_KEY=<the key>
```


## License

serper-mcp-server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.
