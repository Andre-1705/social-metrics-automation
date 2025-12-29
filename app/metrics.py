from __future__ import annotations

import asyncio
from typing import Any

from .config import Settings
from .clients import facebook, instagram, tiktok, whatsapp


async def collect_metrics(settings: Settings) -> list[dict[str, Any]]:
    tasks = [
        asyncio.create_task(facebook.fetch_metrics(settings.facebook_page_access_token, settings.facebook_page_id)),
        asyncio.create_task(instagram.fetch_metrics(settings.instagram_access_token, settings.instagram_business_id)),
        asyncio.create_task(tiktok.fetch_metrics(settings.tiktok_access_token)),
        asyncio.create_task(whatsapp.fetch_metrics(settings.whatsapp_token, settings.whatsapp_phone_number_id)),
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    normalized: list[dict[str, Any]] = []
    for result in results:
        if isinstance(result, Exception):
            normalized.append({"status": "error", "detail": str(result)})
        else:
            normalized.append(result)
    return normalized
