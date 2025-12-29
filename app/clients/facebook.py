from __future__ import annotations

from typing import Any
from datetime import datetime, timedelta

import httpx

GRAPH_API_VERSION = "v21.0"
GRAPH_BASE_URL = f"https://graph.facebook.com/{GRAPH_API_VERSION}"


def _error_payload(platform: str, exc: httpx.HTTPStatusError) -> dict[str, str]:
    response = exc.response
    try:
        detail = response.json()
    except Exception:
        detail = response.text
    return {
        "platform": platform,
        "status": "error",
        "code": str(response.status_code),
        "detail": str(detail),
        "url": str(response.url),
    }


async def verify_token(token: str | None, page_id: str | None) -> dict[str, Any]:
    """Verifica que el token y page_id sean válidos."""
    if not token or not page_id:
        return {"platform": "facebook", "status": "invalid", "reason": "missing credentials"}
    
    url = f"{GRAPH_BASE_URL}/{page_id}"
    params = {"fields": "name,fan_count,access_token", "access_token": token}
    
    async with httpx.AsyncClient(timeout=10) as client:
        try:
            response = await client.get(url, params=params)
            response.raise_for_status()
            body = response.json()
            return {
                "platform": "facebook",
                "status": "valid",
                "page_name": body.get("name"),
                "fan_count": body.get("fan_count"),
                "page_id": page_id
            }
        except httpx.HTTPStatusError as exc:
            return _error_payload("facebook", exc)
        except Exception as e:
            return {"platform": "facebook", "status": "error", "detail": str(e)}


async def publish_post(
    token: str | None, 
    page_id: str | None, 
    message: str,
    image_url: str | None = None,
    link: str | None = None
) -> dict[str, Any]:
    """Publica un post en Facebook con soporte para texto, imagen y link."""
    if not token or not page_id:
        return {"platform": "facebook", "status": "skipped", "reason": "missing credentials"}

    # Si hay imagen, usar endpoint de photos, si no, usar feed
    if image_url:
        url = f"{GRAPH_BASE_URL}/{page_id}/photos"
        payload = {
            "url": image_url,
            "caption": message,
            "access_token": token
        }
    else:
        url = f"{GRAPH_BASE_URL}/{page_id}/feed"
        payload = {
            "message": message,
            "access_token": token
        }
        if link:
            payload["link"] = link
    
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            response = await client.post(url, data=payload)
            response.raise_for_status()
            body = response.json()
            return {
                "platform": "facebook",
                "status": "posted",
                "post_id": body.get("id"),
                "response": body
            }
        except httpx.HTTPStatusError as exc:
            return _error_payload("facebook", exc)
        except Exception as e:
            return {"platform": "facebook", "status": "error", "detail": str(e)}


async def fetch_metrics(token: str | None, page_id: str | None) -> dict[str, Any]:
    """Obtiene métricas de la página de Facebook."""
    if not token or not page_id:
        return {"platform": "facebook", "status": "skipped", "reason": "missing credentials"}

    # Obtener información básica de la página
    page_url = f"{GRAPH_BASE_URL}/{page_id}"
    page_params = {
        "fields": "name,fan_count,followers_count,engagement",
        "access_token": token
    }
    
    # Obtener insights (métricas) de los últimos 7 días
    since = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    until = datetime.now().strftime("%Y-%m-%d")
    
    insights_url = f"{GRAPH_BASE_URL}/{page_id}/insights"
    insights_params = {
        "metric": "page_impressions,page_post_engagements,page_fans,page_views_total",
        "period": "day",
        "since": since,
        "until": until,
        "access_token": token
    }
    
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            # Obtener datos de página
            page_response = await client.get(page_url, params=page_params)
            page_response.raise_for_status()
            page_data = page_response.json()
            
            # Obtener insights
            insights_response = await client.get(insights_url, params=insights_params)
            insights_response.raise_for_status()
            insights_data = insights_response.json()
            
            return {
                "platform": "facebook",
                "status": "ok",
                "page_info": page_data,
                "insights": insights_data.get("data", []),
                "period": {"since": since, "until": until}
            }
        except httpx.HTTPStatusError as exc:
            return _error_payload("facebook", exc)
        except Exception as e:
            return {"platform": "facebook", "status": "error", "detail": str(e)}
