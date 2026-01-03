from __future__ import annotations

import asyncio
from typing import Any, Iterable

from .config import Settings
from .clients import facebook, instagram, tiktok, whatsapp


async def publish_message(
    message: str,
    settings: Settings,
    platforms: Iterable[str] | None = None,
    image_url: str | None = None,
    link: str | None = None
) -> list[dict[str, Any]]:
    """Publica un mensaje en las plataformas seleccionadas."""
    targets = set(platforms) if platforms else {"facebook", "instagram", "tiktok", "whatsapp"}
    tasks: list[asyncio.Task] = []

    if "facebook" in targets:
        tasks.append(
            asyncio.create_task(
                facebook.publish_post(
                    settings.facebook_page_access_token,
                    settings.facebook_page_id,
                    message,
                    image_url=image_url,
                    link=link
                )
            )
        )
    if "instagram" in targets:
        tasks.append(
            asyncio.create_task(
                instagram.publish_post(
                    settings.instagram_access_token,
                    settings.instagram_business_id,
                    message,
                    image_url=image_url
                )
            )
        )
    if "tiktok" in targets:
        tasks.append(
            asyncio.create_task(
                tiktok.publish_post(settings.tiktok_access_token, message)
            )
        )
    if "whatsapp" in targets:
        tasks.append(
            asyncio.create_task(
                whatsapp.send_message(
                    settings.whatsapp_token,
                    settings.whatsapp_phone_number_id,
                    message
                )
            )
        )

    if not tasks:
        return []

    results = await asyncio.gather(*tasks, return_exceptions=True)
    normalized: list[dict[str, Any]] = []
    for result in results:
        if isinstance(result, Exception):
            normalized.append({"status": "error", "detail": str(result)})
        else:
            normalized.append(result)
    return normalized


async def verify_connections(settings: Settings) -> list[dict[str, Any]]:
    """Verifica las conexiones con todas las plataformas configuradas."""
    tasks = []
    
    if settings.facebook_page_access_token and settings.facebook_page_id:
        tasks.append(
            asyncio.create_task(
                facebook.verify_token(
                    settings.facebook_page_access_token,
                    settings.facebook_page_id
                )
            )
        )
    
    if settings.instagram_access_token and settings.instagram_business_id:
        tasks.append(
            asyncio.create_task(
                instagram.verify_token(
                    settings.instagram_access_token,
                    settings.instagram_business_id
                )
            )
        )

    if settings.tiktok_access_token:
        tasks.append(asyncio.create_task(tiktok.verify_token(settings.tiktok_access_token)))
    
    if not tasks:
        return [{"status": "no_credentials", "message": "No hay credenciales configuradas"}]
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    normalized: list[dict[str, Any]] = []
    for result in results:
        if isinstance(result, Exception):
            normalized.append({"status": "error", "detail": str(result)})
        else:
            normalized.append(result)
    return normalized
