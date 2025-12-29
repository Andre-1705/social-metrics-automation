import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):
    facebook_page_access_token: str | None = os.getenv("FACEBOOK_PAGE_ACCESS_TOKEN")
    facebook_page_id: str | None = os.getenv("FACEBOOK_PAGE_ID")
    instagram_access_token: str | None = os.getenv("INSTAGRAM_ACCESS_TOKEN")
    instagram_business_id: str | None = os.getenv("INSTAGRAM_BUSINESS_ID")
    tiktok_access_token: str | None = os.getenv("TIKTOK_ACCESS_TOKEN")
    whatsapp_token: str | None = os.getenv("WHATSAPP_TOKEN")
    whatsapp_phone_number_id: str | None = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
    default_timezone: str = os.getenv("DEFAULT_TIMEZONE", "UTC")
    privacy_policy_url: str = os.getenv("PRIVACY_POLICY_URL", "https://polit-priv.vercel.app/")
    terms_of_service_url: str = os.getenv(
        "TERMS_OF_SERVICE_URL",
        os.getenv("PRIVACY_POLICY_URL", "https://polit-priv.vercel.app/")
    )
    support_contact_email: str | None = os.getenv("SUPPORT_CONTACT_EMAIL")
    public_base_url: str = os.getenv("PUBLIC_BASE_URL", "http://localhost:8000")


def get_settings() -> Settings:
    return Settings()
