import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):
    # Meta App Credentials
    facebook_app_id: str | None = os.getenv("FACEBOOK_APP_ID")
    facebook_app_secret: str | None = os.getenv("FACEBOOK_APP_SECRET")
    
    # Facebook Page
    facebook_page_access_token: str | None = os.getenv("FACEBOOK_PAGE_ACCESS_TOKEN")
    facebook_page_id: str | None = os.getenv("FACEBOOK_PAGE_ID")
    
    # Instagram Business
    instagram_access_token: str | None = os.getenv("INSTAGRAM_ACCESS_TOKEN")
    instagram_business_id: str | None = os.getenv("INSTAGRAM_BUSINESS_ID")
    
    # Meta Webhooks
    meta_webhook_verify_token: str | None = os.getenv("META_WEBHOOK_VERIFY_TOKEN")
    
    # TikTok
    tiktok_access_token: str | None = os.getenv("TIKTOK_ACCESS_TOKEN")
    
    # WhatsApp Business
    whatsapp_token: str | None = os.getenv("WHATSAPP_TOKEN")
    whatsapp_phone_number_id: str | None = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
    
    # General Settings
    default_timezone: str = os.getenv("DEFAULT_TIMEZONE", "UTC")
    
    # Public URLs (Required by Meta)
    public_base_url: str = os.getenv("PUBLIC_BASE_URL", "http://localhost:8000")
    privacy_policy_url: str = os.getenv("PRIVACY_POLICY_URL", "https://polit-priv.vercel.app/")
    terms_of_service_url: str = os.getenv(
        "TERMS_OF_SERVICE_URL",
        os.getenv("PRIVACY_POLICY_URL", "https://polit-priv.vercel.app/")
    )
    eliminacion_de_datos_url: str = os.getenv(
        "ELIMINACION_DE_DATOS_URL",
        "https://polit-priv.vercel.app/elimindatos"
    )
    
    # Contact and Support
    support_contact_email: str | None = os.getenv("SUPPORT_CONTACT_EMAIL")


def get_settings() -> Settings:
    return Settings()

