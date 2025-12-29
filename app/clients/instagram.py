from __future__ import annotations

from typing import Any
from datetime import datetime, timedelta
import asyncio

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


async def verify_token(token: str | None, business_id: str | None) -> dict[str, Any]:
    """Verifica que el token y business account sean válidos."""
    if not token or not business_id:
        return {"platform": "instagram", "status": "invalid", "reason": "missing credentials"}
    
    url = f"{GRAPH_BASE_URL}/{business_id}"
    params = {"fields": "username,name,followers_count,media_count", "access_token": token}
    
    async with httpx.AsyncClient(timeout=10) as client:
        try:
            response = await client.get(url, params=params)
            response.raise_for_status()
            body = response.json()
            return {
                "platform": "instagram",
                "status": "valid",
                "username": body.get("username"),
                "name": body.get("name"),
                "followers_count": body.get("followers_count"),
                "media_count": body.get("media_count")
            }
        except httpx.HTTPStatusError as exc:
            return _error_payload("instagram", exc)
        except Exception as e:
            return {"platform": "instagram", "status": "error", "detail": str(e)}


async def publish_post(
    token: str | None,
    business_id: str | None,
    message: str,
    image_url: str | None = None,
    is_carousel: bool = False
) -> dict[str, Any]:
    """Publica un post en Instagram. Requiere imagen_url para posts."""
    if not token or not business_id:
        return {"platform": "instagram", "status": "skipped", "reason": "missing credentials"}
    
    if not image_url:
        return {
            "platform": "instagram",
            "status": "error",
            "reason": "Instagram requiere image_url para publicar posts"
        }
    
    async with httpx.AsyncClient(timeout=60) as client:
        try:
            # Paso 1: Crear el contenedor de medios
            create_url = f"{GRAPH_BASE_URL}/{business_id}/media"
            create_payload = {
                "image_url": image_url,
                "caption": message,
                "access_token": token
            }
            
            create_response = await client.post(create_url, data=create_payload)
            create_response.raise_for_status()
            creation_data = create_response.json()
            container_id = creation_data.get("id")
            
            if not container_id:
                return {
                    "platform": "instagram",
                    "status": "error",
                    "reason": "No se obtuvo container_id",
                    "response": creation_data
                }
            
            # Paso 2: Esperar un momento para que se procese
            await asyncio.sleep(2)
            
            # Paso 3: Publicar el contenedor
            publish_url = f"{GRAPH_BASE_URL}/{business_id}/media_publish"
            publish_payload = {
                "creation_id": container_id,
                "access_token": token
            }
            
            publish_response = await client.post(publish_url, data=publish_payload)
            publish_response.raise_for_status()
            publish_data = publish_response.json()
            
            return {
                "platform": "instagram",
                "status": "posted",
                "media_id": publish_data.get("id"),
                "container_id": container_id,
                "response": publish_data
            }
            
        except httpx.HTTPStatusError as exc:
            return _error_payload("instagram", exc)
        except Exception as e:
            return {"platform": "instagram", "status": "error", "detail": str(e)}


async def fetch_metrics(token: str | None, business_id: str | None) -> dict[str, Any]:
    """Obtiene métricas de la cuenta de Instagram Business."""
    if not token or not business_id:
        return {"platform": "instagram", "status": "skipped", "reason": "missing credentials"}
    
    # Obtener información de la cuenta
    account_url = f"{GRAPH_BASE_URL}/{business_id}"
    account_params = {
        "fields": "username,name,followers_count,follows_count,media_count,profile_picture_url",
        "access_token": token
    }
    
    # Obtener insights de la cuenta
    since = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    until = datetime.now().strftime("%Y-%m-%d")
    
    insights_url = f"{GRAPH_BASE_URL}/{business_id}/insights"
    insights_params = {
        "metric": "impressions,reach,profile_views,follower_count",
        "period": "day",
        "since": since,
        "until": until,
        "access_token": token
    }
    
    # Obtener medios recientes
    media_url = f"{GRAPH_BASE_URL}/{business_id}/media"
    media_params = {
        "fields": "id,caption,media_type,media_url,timestamp,like_count,comments_count",
        "limit": 10,
        "access_token": token
    }
    
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            # Obtener datos de cuenta
            account_response = await client.get(account_url, params=account_params)
            account_response.raise_for_status()
            account_data = account_response.json()
            
            # Obtener insights
            insights_response = await client.get(insights_url, params=insights_params)
            insights_response.raise_for_status()
            insights_data = insights_response.json()
            
            # Obtener medios recientes
            media_response = await client.get(media_url, params=media_params)
            media_response.raise_for_status()
            media_data = media_response.json()
            
            return {
                "platform": "instagram",
                "status": "ok",
                "account_info": account_data,
                "insights": insights_data.get("data", []),
                "recent_media": media_data.get("data", []),
                "period": {"since": since, "until": until}
            }
        except httpx.HTTPStatusError as exc:
            return _error_payload("instagram", exc)
        except Exception as e:
            return {"platform": "instagram", "status": "error", "detail": str(e)}
