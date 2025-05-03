from pydantic import BaseModel

class UserCreate(BaseModel):
    nickname: str
    password: str
