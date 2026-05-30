from pydantic import BaseModel, Field

class UserRegisterValidator(BaseModel):
    user_name: str = Field(..., min_length=3)
    age: int = Field(..., gt=0)
    uf: str

