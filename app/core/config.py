from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "TabGen"
    
    POSTGRES_USER: str = "tabgenuser"
    POSTGRES_PASSWORD: str = "qwerty"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DBNAME: str = "tabgen"
    POSTGRESQL_URI: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DBNAME}"


settings = Settings()
