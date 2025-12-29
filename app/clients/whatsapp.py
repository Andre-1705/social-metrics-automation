from __future__ import annotations

from typing import Any

import httpx


async def send_message(token: str | None, phone_number_id: str | None, message: str) -> dict[str, Any]:
    if not token or not phone_number_id:
        return {"platform": "whatsapp", "status": "skipped", "reason": "missing credentials"}

    url = f"https://graph.facebook.com/v19.0/{phone_number_id}/messages"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"messaging_product": "whatsapp", "to": "YOUR_RECIPIENT", "type": "text", "text": {"body": message}}
    async with httpx.AsyncClient(timeout=10, headers=headers) as client:
        response = await client.post(url, json=payload)
        response.raise_for_status()
        body = response.json()
    return {"platform": "whatsapp", "status": "sent", "response": body}


async def fetch_metrics(token: str | None, phone_number_id: str | None) -> dict[str, Any]:
    if not token or not phone_number_id:
        return {"platform": "whatsapp", "status": "skipped", "reason": "missing credentials"}

    # WhatsApp Cloud API does not expose detailed analytics; returning placeholder.
    return {"platform": "whatsapp", "status": "ok", "metrics": {"messages_sent": None, "notes": "Add webhook-based tracking"}}
