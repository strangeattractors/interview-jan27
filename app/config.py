from pydantic import EmailStr
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    ENV_STATE: str = "dev"
    DROP_ENVS: list[str] = ["test"]


class Config(BaseConfig):
    DB_URL: str = "sqlite+aiosqlite:///test.db"
    SECRET_KEY: str = "123"
    ALGORITHM: str = "HS512"
    TOKEN_EXPIRE_SECONDS: int = 3600
    RESET_EXPIRE_SECONDS: int = 300
    TOKEN_PATH: str = "api/v1/auth/token"
    ADMIN_EMAIL: EmailStr = "admin@sample.com"
    ADMIN_PASSWORD: str = "123"
    ADMIN_EMAIL_TOKEN: str = "123"
    LOG_LEVEL: str = "DEBUG"
    RATE_LIMITS: tuple[int, int] = (10, 60)


class TestConfig(Config):
    DB_URL: str = "sqlite+aiosqlite:///test.db"
    LOG_LEVEL: str = "DEBUG"


class DevConfig(Config):
    DB_URL: str = "sqlite+aiosqlite:///dev.db"
    TOKEN_EXPIRE_SECONDS: int = 3600 * 24
    RESET_EXPIRE_SECONDS: int = 3600
    LOG_LEVEL: str = "DEBUG"
    ADMIN_EMAIL: EmailStr = "test@test.com"
    ADMIN_EMAIL_TOKEN: str = "dummy_DEV_ADMIN_EMAIL_TOKEN"
    ADMIN_PASSWORD: str = "dev_password"


def get_config(env: str = "dev") -> TestConfig | DevConfig:
    env = env or "dev"
    return {"test": TestConfig, "dev": DevConfig}[env](ENV_STATE=env)


config = get_config()
