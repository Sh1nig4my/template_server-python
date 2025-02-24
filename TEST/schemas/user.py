from pydantic import BaseModel

# Schema per la creazione di un utente (input)
class UserCreate(BaseModel):
    email: str
    username: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

# Schema per la visualizzazione di un utente (output)
class UserResponse(BaseModel):
    id: int
    email: str
    username: str

    class Config:
        orm_mode = True

