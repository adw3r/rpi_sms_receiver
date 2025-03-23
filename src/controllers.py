import serial
import time

from src import config
from src.config import logger


class SmsController:
    com_port = serial.Serial(config.SIM_SOCKET, baudrate=config.BAUDRATE, timeout=1)

    def _send_at(self, command, delay=1):
        logger.info(f'{command = }')
        self.com_port.write((command + "\r\n").encode())
        time.sleep(delay)
        response = self.com_port.read(self.com_port.inWaiting()).decode()
        return response

    def get_messages(self, folder='all'):
        """
        at+cmgl="all”

        :return:
        """
        return self._send_at(f'at+cmgl="{folder}"'.upper(), .5)
