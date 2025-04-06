from . import server


def main():
    import asyncio
    asyncio.run(server.main())


__all__ = ["main"]
