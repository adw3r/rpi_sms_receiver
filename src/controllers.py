import time

import serial

from src import config
from src.config import logger


class SmsController:
    com_port = serial.Serial(config.SIM_SOCKET, baudrate=config.BAUDRATE, timeout=1)

    def __init__(self):
        self._send_at("at+cmgf=1")

    def _send_at(self, command, delay=1):
        logger.info(f"{command = }")
        self.com_port.write((command + "\r\n").encode())
        time.sleep(delay)
        response = self.com_port.read(self.com_port.inWaiting()).decode()
        logger.info(response)
        return response

    def delete_specific_message(self, index: str | int):
        return self._send_at(f"AT+CMGD={index}")

    def get_specific_message(self, index: str | int):
        return self._send_at(f"AT+CMGR={index}")

    def get_messages(self, folder="all"):
        """
        at+cmgl="all”

        :return:
        """
        return self._send_at(f'at+cmgl="{folder}"'.upper(), 0.5)
