from pydantic import BaseModel

class UserCreate(BaseModel):
    login: str
    password: str

class UserOut(BaseModel):
    id: int
    login: str

    class Config:
        from_attributes = True
