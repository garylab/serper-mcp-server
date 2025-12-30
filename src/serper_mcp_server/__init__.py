import asyncio
import argparse


def main():
    from . import server
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--q", type=str, help="The query to search for")
    # args = parser.parse_args()
    asyncio.run(server.main())


__all__ = ["main"]
