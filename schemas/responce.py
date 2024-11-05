from pydantic import BaseModel

class ResponseModel(BaseModel):
    user_id: int
    timestamp: str
    client_version: str
    message: str