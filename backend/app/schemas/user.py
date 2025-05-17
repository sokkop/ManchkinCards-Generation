from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserInDB(User):
    hashed_password: str

class UserLogin(BaseModel):
    username: str
    password: str
