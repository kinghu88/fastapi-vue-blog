import secrets
from typing import List

from pydantic import BaseSettings, AnyHttpUrl

import os


class Settings(BaseSettings):
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    LOG_PATH = os.path.join(BASEDIR, 'logs')
    BACKEND_CORS_ORIGINS: List = ['*']

    # SQLALCHEMY_DATABASE_URI: str = f'sqlite:///{BASEDIR}/fastapi-vue-blog.db'
    # SQLALCHEMY_DATABASE_URI: str = 'mysql+aiomysql://root:@localhost/fastapi_sqlalchemy_async'
    SQLALCHEMY_DATABASE_URI: str = 'mysql+aiomysql://root:Grandhonor12306@192.168.3.100:10000/xqh'
    SECRET_KEY: str = secrets.token_urlsafe(32)

    # 30 minutes
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '[%(asctime)s] %(levelname)s %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
            'standard': {
                'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
            'logfile': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(BASEDIR, 'logs', 'debug.log'),
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 7,
                'formatter': 'standard'
            },
            'db_logfile': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'db.log'),
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 7,
                'formatter': 'standard'
            },
            'run': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'run.log'),
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 7,
                'formatter': 'standard'
            },
            'error': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'error.log'),
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 7,
                'formatter': 'standard'
            },
            'test': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'test.log'),
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 7,
                'formatter': 'standard'
            },
        },
        'loggers': {
            'fastapi': {
                'handlers': ['run'],
                'level': 'DEBUG',
                'propagate': False
            },
            'uvicorn.access': {
                'handlers': ['run'],
                'level': 'INFO',
                'propagate': False
            },
            'uvicorn.error': {
                'handlers': ['error'],
                'level': 'INFO',
                'propagate': False
            },
            'test': {
                'handlers': ['logfile'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'database': {
                'handlers': ['db_logfile'],
                'level': 'DEBUG',
                'propagate': False,
            },
        },
    }


settings = Settings()

# if not os.path.exists(settings.LOG_PATH):
#     os.makedirs(settings.LOG_PATH)
