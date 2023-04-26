import os


class BaseConfig:
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test_db.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    DEBUG = False


app_config = ProductionConfig() if os.getenv(
    "ENV") == "production" else DevelopmentConfig()
