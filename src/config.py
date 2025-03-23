import logging
import os
import pathlib
import sys

from dotenv import load_dotenv
from loguru import logger

load_dotenv()
ROOT_DIR = pathlib.Path(__file__).parent.parent

# sim config
SIM_SOCKET = os.environ['SIM_SOCKET']
BAUDRATE = os.environ['BAUDRATE']


# fastapi config
APP_PORT = int(os.environ['APP_PORT'])
APP_HOST = os.environ['APP_HOST']


# logging
logger.remove()
# logging.disable()
LOGGING_FORMAT = (
    "<level>{time:YYYY-MM-DD HH:mm:ss.SSS}</level> "
    "<level>{level}</level>: "
    "<level>{name}</level> - "
    "<level>{message}</level>"
)

logger.add(
    ROOT_DIR / "logs" / "log_{time:YYYY-MM-DD}.log",
    format=LOGGING_FORMAT,
    level="DEBUG",
    mode="a",
    retention="5 days",
)
logger.add(sys.stdout, format=LOGGING_FORMAT)
