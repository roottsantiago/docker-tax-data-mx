from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_STR: str = "/api/v1"
    PROYECT_NAME: str = "Tax-Data-MX"

    class Config:
        case_sensitive = True


settings = Settings()