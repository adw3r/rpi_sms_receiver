import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, Response

from src import config, controllers, serializers

sms_controller = controllers.SmsController()

app = FastAPI(title='RPI sms receiver')


@app.get("/")
async def root():
    return RedirectResponse("/docs")


@app.get("/messages", tags=["Messages"])
async def get_messages(folder="all"):
    messages = sms_controller.get_messages(folder)
    messages = serializers.serialize_all_messages(messages)
    return messages


@app.get('/messages/{message_id}', tags=["Messages"])
async def get_specific_message(message_id: str | int):
    try:
        raw_message = sms_controller.get_specific_message(message_id)
        return serializers.serialize_single_message(raw_message)
    except Exception as error:
        from src.config import logger
        logger.error(error)
        return Response(status_code=500, content='error')


@app.delete('/messages/{message_id}', tags=["Messages"])
async def delete_specific_message(message_id: str | int):
    return sms_controller.delete_specific_message(message_id)

def main():
    uvicorn.run("src.main:app", host=config.APP_HOST, port=config.APP_PORT)


if __name__ == "__main__":
    main()
