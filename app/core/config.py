import os
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    RETOOL_API_KEY: str = os.environ.get(
        "RETOOL_API_KEY", "")
    RETOOL_POSTGRES_URL: str = os.environ.get(
        "RETOOL_POSTGRES_URL", "")
    OPENAI_API_KEY: str = os.environ.get(
        "OPENAI_API_KEY", "")
    USER_ID: str = os.environ.get("USER_ID", "")
    PROJECT_ID: str = os.environ.get("PROJECT_ID", "")