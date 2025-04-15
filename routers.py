import uvicorn
from fastapi import FastAPI
from constants.constants import *
from model.datamodel import MattbotDataModel
from handlers import Handlers as MattbotHandler

app = FastAPI()


@app.get("/")
def version():
    return {"Version": 3.0}


@app.post("/chat")
def mattbot_query(user_response_received: MattbotDataModel):
    bot_response = MattbotHandler().handle_user_query(user_response_received)
    return {"bot_response": bot_response}


if __name__ == "__main__":
    uvicorn.run(APPLICATION_NAME, host=IP_ADDRESS, port=PORT, reload=True)
