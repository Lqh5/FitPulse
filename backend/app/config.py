"""
FitPulse Backend Configuration
Reads from environment variables / .env file.
"""
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # App
    APP_ENV: str = "development"
    DEBUG: bool = True

    # Anthropic Claude
    ANTHROPIC_API_KEY: str = ""

    # MySQL
    DATABASE_URL: str = "mysql+pymysql://fitpulse:fitpulse2024@localhost:3306/fitpulse"

    # Chroma
    CHROMA_HOST: str = "localhost"
    CHROMA_PORT: int = 8000

    # MinIO
    MINIO_ENDPOINT: str = "localhost:9000"
    MINIO_ROOT_USER: str = "fitpulse"
    MINIO_ROOT_PASSWORD: str = "fitpulse2024"
    MINIO_BUCKET: str = "fitpulse"

    # JWT
    JWT_SECRET_KEY: str = "change-me-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 1440

    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()