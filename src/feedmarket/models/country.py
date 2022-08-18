from pydantic import BaseModel


class CountryBase(BaseModel):
    name: str


class Country(CountryBase):
    id: int

    class Config:
        orm_mode = True


class CountryCreate(CountryBase):
    pass


class CountryUpdate(CountryBase):
    pass
