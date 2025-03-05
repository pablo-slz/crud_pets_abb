from pydantic import BaseModel

class Pet(BaseModel):
    id_pet: int
    name: str
    age: int
    owner: str
