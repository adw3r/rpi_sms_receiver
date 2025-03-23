import uvicorn
from fastapi import FastAPI

from src import config, controllers

sms_controller = controllers.SmsController()

app = FastAPI()


@app.get("/messages", tags=['Messages'])
async def get_messages(folder="all"):
    return sms_controller.get_messages(folder)


def main():
    uvicorn.run("src.main:app", host=config.APP_HOST, port=config.APP_PORT)


if __name__ == "__main__":
    main()
