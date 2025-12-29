from __future__ import annotations

from typing import Any

import httpx


async def publish_post(token: str | None, message: str) -> dict[str, Any]:
    if not token:
        return {"platform": "tiktok", "status": "skipped", "reason": "missing credentials"}

    url = "https://open.tiktokapis.com/v2/post/publish/"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"text": message}
    async with httpx.AsyncClient(timeout=10, headers=headers) as client:
        response = await client.post(url, json=payload)
        response.raise_for_status()
        body = response.json()
    return {"platform": "tiktok", "status": "posted", "response": body}


async def fetch_metrics(token: str | None) -> dict[str, Any]:
    if not token:
        return {"platform": "tiktok", "status": "skipped", "reason": "missing credentials"}

    url = "https://open.tiktokapis.com/v2/insights/user/"
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient(timeout=10, headers=headers) as client:
        response = await client.get(url)
        response.raise_for_status()
        body = response.json()
    return {"platform": "tiktok", "status": "ok", "metrics": body}
