from pydantic import BaseSettings

class Settings(BaseSettings):
    # JWT Settings (no defaults for sensitive data!)
    SECRET_KEY: str
    ALGORITHM: str = "HS256"  # Non-sensitive default OK
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Non-sensitive default OK
    
    # MySQL Settings (no hardcoded values!)
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'  # Add encoding for reliability

settings = Settings()