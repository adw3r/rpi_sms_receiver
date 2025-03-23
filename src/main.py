import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src import config, controllers

sms_controller = controllers.SmsController()

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse("/docs")


@app.get("/messages", tags=["Messages"])
async def get_messages(folder="all"):
    return sms_controller.get_messages(folder)


@app.get('/messages/{message_id}')
async def get_specific_message(message_id: str | int):
    return sms_controller.get_specific_message(message_id)


@app.delete('/messages/{message_id}')
async def delete_specific_message(message_id: str | int):
    return sms_controller.delete_specific_message(message_id)

def main():
    uvicorn.run("src.main:app", host=config.APP_HOST, port=config.APP_PORT)


if __name__ == "__main__":
    main()
