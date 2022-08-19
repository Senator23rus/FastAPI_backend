from pydantic import BaseModel


class IndustryBase(BaseModel):
    name: str


class Industry(IndustryBase):
    id: int

    class Config:
        orm_mode = True
