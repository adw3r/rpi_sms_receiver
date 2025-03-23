import os
import pathlib
from dotenv import load_dotenv

load_dotenv()
ROOT_DIR = pathlib.Path(__file__).parent.parent

# sim config
SIM_SOCKET = os.environ['SIM_SOCKET']
BAUDRATE = os.environ['BAUDRATE']


# fastapi config
APP_PORT = os.environ['APP_PORT']
APP_HOST = os.environ['APP_HOST']
