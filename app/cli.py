from __future__ import annotations

import asyncio
from typing import Optional

import typer
import uvicorn

from .config import get_settings
from .metrics import collect_metrics
from .publisher import publish_message

cli = typer.Typer(help="Automatiza publicaciones y métricas de RRSS.")


@cli.command()
def publish(message: str, platforms: Optional[str] = typer.Option(None, help="Lista separada por comas: facebook,instagram,tiktok,whatsapp")) -> None:
    settings = get_settings()
    selected = [p.strip() for p in platforms.split(",")] if platforms else None
    results = asyncio.run(publish_message(message, settings, selected))
    typer.echo(results)


@cli.command()
def metrics() -> None:
    settings = get_settings()
    data = asyncio.run(collect_metrics(settings))
    typer.echo(data)


@cli.command()
def serve(host: str = "0.0.0.0", port: int = 8000, reload: bool = True) -> None:
    uvicorn.run("app.main:app", host=host, port=port, reload=reload)


if __name__ == "__main__":
    cli()
