from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Template"
    DEBUG: bool = False
    API_V1_STR: str = "/api/v1"

    model_config = {"env_file": ".env"}


settings = Settings()
