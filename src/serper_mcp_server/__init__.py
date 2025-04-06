import asyncio
import argparse
from . import server


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--q", type=str, help="The query to search for")
    # args = parser.parse_args()
    asyncio.run(server.main())


__all__ = ["main"]
