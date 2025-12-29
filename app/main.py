from __future__ import annotations

from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uuid
from datetime import datetime, timezone

from .config import Settings, get_settings
from .metrics import collect_metrics
from .publisher import publish_message, verify_connections

app = FastAPI(
    title="Social Metrics Automation",
    description="API para publicar y obtener métricas de Facebook, Instagram, TikTok y WhatsApp",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PublishRequest(BaseModel):
    message: str
    platforms: list[str] | None = None
    image_url: str | None = None
    link: str | None = None


class DataDeletionRequest(BaseModel):
    platform: str | None = None  # e.g., "facebook", "instagram"
    user_id: str | None = None   # optional user identifier
    signed_request: str | None = None  # Meta can send this param


@app.get("/")
async def root(settings: Settings = Depends(get_settings)) -> dict:
    """Endpoint raíz con información de la API."""
    return {
        "name": "Social Metrics Automation API",
        "version": "1.0.0",
        "privacy_policy": settings.privacy_policy_url,
        "terms_of_service": settings.terms_of_service_url,
        "support_contact_email": settings.support_contact_email,
        "endpoints": {
            "health": "/health",
            "verify": "/verify",
            "publish": "/publish",
            "metrics": "/metrics",
            "data_deletion": "/data-deletion"
        }
    }


@app.get("/health")
async def health() -> dict[str, str]:
    """Verifica el estado de la API."""
    return {"status": "ok"}


@app.get("/verify")
async def verify(settings: Settings = Depends(get_settings)) -> dict:
    """Verifica las conexiones con Meta (Facebook/Instagram)."""
    results = await verify_connections(settings)
    return {"connections": results}


@app.post("/publish")
async def publish(payload: PublishRequest, settings: Settings = Depends(get_settings)) -> dict:
    """Publica un mensaje en las plataformas seleccionadas.
    
    Args:
        message: Texto del mensaje
        platforms: Lista de plataformas (facebook, instagram, tiktok, whatsapp). Por defecto todas.
        image_url: URL de imagen (requerido para Instagram)
        link: URL para compartir (solo Facebook)
    """
    results = await publish_message(
        payload.message,
        settings,
        payload.platforms,
        image_url=payload.image_url,
        link=payload.link
    )
    return {"results": results}


@app.get("/metrics")
async def metrics(settings: Settings = Depends(get_settings)) -> dict:
    """Obtiene métricas de todas las plataformas configuradas."""
    data = await collect_metrics(settings)
    return {"results": data}


# Data Deletion (Meta requirement)
@app.get("/data-deletion")
async def data_deletion_get(request: Request, settings: Settings = Depends(get_settings)) -> dict:
    """Handles user data deletion requests (GET).

    For Facebook, Meta may call this endpoint with query parameters like `signed_request` or `user_id`.
    We return a confirmation code and a status URL per Meta's guidance.
    """
    params = dict(request.query_params)
    platform = params.get("platform")
    user_id = params.get("user_id")
    signed_request = params.get("signed_request")

    confirmation_code = uuid.uuid4().hex
    status_url = f"{settings.public_base_url}/data-deletion/status/{confirmation_code}"

    return {
        "status": "received",
        "platform": platform,
        "user_id": user_id,
        "signed_request": signed_request,
        "requested_at": datetime.now(timezone.utc).isoformat(),
        "confirmation_code": confirmation_code,
        "url": status_url,
        "message": "Your data deletion request has been received. If any user data exists, it will be deleted as per our policy."
    }


@app.post("/data-deletion")
async def data_deletion_post(payload: DataDeletionRequest, settings: Settings = Depends(get_settings)) -> dict:
    """Handles user data deletion requests (POST)."""
    confirmation_code = uuid.uuid4().hex
    status_url = f"{settings.public_base_url}/data-deletion/status/{confirmation_code}"

    return {
        "status": "received",
        "platform": payload.platform,
        "user_id": payload.user_id,
        "signed_request": payload.signed_request,
        "requested_at": datetime.now(timezone.utc).isoformat(),
        "confirmation_code": confirmation_code,
        "url": status_url,
        "message": "Your data deletion request has been received. If any user data exists, it will be deleted as per our policy."
    }


@app.get("/data-deletion/status/{code}")
async def data_deletion_status(code: str, settings: Settings = Depends(get_settings)) -> dict:
    """Returns a generic status for a data deletion request.

    Note: This implementation is stateless for simplicity. If you later persist requests,
    you can look up the code and return detailed status.
    """
    return {
        "confirmation_code": code,
        "status": "in_progress",
        "policy": settings.privacy_policy_url,
        "contact": settings.support_contact_email,
        "message": "We received your request. If any user data exists in our systems, it will be deleted per policy within 30 days."
    }
