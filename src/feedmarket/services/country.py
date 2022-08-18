from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import tables
from ..database import get_session
from ..models.country import CountryCreate, CountryUpdate


class CountryService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_id(self, user_id: int, country_id: int) -> tables.Country:
        country = (
            self.session
            .query(tables.Country)
            .filter_by(id=country_id, user_id=user_id, )
            .first()
        )
        if not country:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail={'message': "Не найдено"})
        return country

    def get_list(self, user_id: int, ) -> List[tables.Country]:
        query = (self.session
                 .query(tables.Country)
                 .filter_by(user_id=user_id)
                 )
        country = query.all()
        return country

    def get_by_id(self, user_id: int, country_id: int) -> tables.Country:
        return self.get_id(user_id, country_id)

    # def create_many(self, user_id: int, country_data: List[CountryCreate]) -> List[tables.Country]:
    #     coutnry = [
    #         tables.Country(
    #             **countrys_data.dict(),
    #             user_id=user_id,
    #         )
    #         for countrys_data in country_data
    #     ]
    #     self.session.add_all(coutnry)
    #     self.session.commit()
    #     return coutnry

    def create(self, user_id: int, country_data: CountryCreate) -> tables.Country:
        country = tables.Country(
                **country_data.dict(),
                user_id=user_id,
            )
        self.session.add(country)
        self.session.commit()
        return country

    def update(self, user_id: int, country_id: int, country_data: CountryUpdate) -> tables.Country:
        country = self.get_id(user_id, country_id)
        for field, value in country_data:
            setattr(country, field, value)
        self.session.commit()
        return country

    def delete(self, user_id: int, country_id: int):
        country = self.get_id(user_id, country_id)
        self.session.delete(country)
        self.session.commit()