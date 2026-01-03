from __future__ import annotations

from typing import Any

import httpx

BASE_URL = "https://open.tiktokapis.com/v2"


def _error_payload(exc: httpx.HTTPStatusError) -> dict[str, Any]:
    resp = exc.response
    try:
        detail = resp.json()
    except Exception:
        detail = resp.text
    return {
        "platform": "tiktok",
        "status": "error",
        "code": str(resp.status_code),
        "detail": detail,
        "url": str(resp.url),
    }


async def verify_token(token: str | None) -> dict[str, Any]:
    if not token:
        return {"platform": "tiktok", "status": "invalid", "reason": "missing credentials"}

    url = f"{BASE_URL}/user/info/"
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient(timeout=10, headers=headers) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            body = response.json()
            return {
                "platform": "tiktok",
                "status": "valid",
                "user": body.get("data") or body,
            }
        except httpx.HTTPStatusError as exc:
            return _error_payload(exc)
        except Exception as exc:  # pragma: no cover - network failures
            return {"platform": "tiktok", "status": "error", "detail": str(exc)}


async def publish_post(token: str | None, message: str) -> dict[str, Any]:
    if not token:
        return {"platform": "tiktok", "status": "skipped", "reason": "missing credentials"}

    url = f"{BASE_URL}/post/publish/"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"text": message}

    async with httpx.AsyncClient(timeout=15, headers=headers) as client:
        try:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            body = response.json()
            return {"platform": "tiktok", "status": "posted", "response": body}
        except httpx.HTTPStatusError as exc:
            return _error_payload(exc)
        except Exception as exc:  # pragma: no cover - network failures
            return {"platform": "tiktok", "status": "error", "detail": str(exc)}


async def fetch_metrics(token: str | None) -> dict[str, Any]:
    if not token:
        return {"platform": "tiktok", "status": "skipped", "reason": "missing credentials"}

    url = f"{BASE_URL}/insights/user/"
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient(timeout=15, headers=headers) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            body = response.json()
            return {"platform": "tiktok", "status": "ok", "metrics": body}
        except httpx.HTTPStatusError as exc:
            return _error_payload(exc)
        except Exception as exc:  # pragma: no cover - network failures
            return {"platform": "tiktok", "status": "error", "detail": str(exc)}
