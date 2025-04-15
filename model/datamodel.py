from pydantic import BaseModel


class MattbotDataModel(BaseModel):
    response: str
