from typing import List, Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from ..models.auth import User
from ..models.country import Country, CountryCreate, CountryUpdate
from ..services.auth import get_current_user
from ..services.country import CountryService

router = APIRouter(
    prefix='/country',
    tags=['Страны производители'],
)


@router.get('/', response_model=List[Country], )
def get_country(
        user: User = Depends(get_current_user),
        service: CountryService = Depends()
):
    """
    Получение списка стран производителей.
    """
    return service.get_list(user_id=user.id)


@router.post('/', response_model=Country)
def create_country(
        country_data: CountryCreate,
        user: User = Depends(get_current_user),
        service: CountryService = Depends(),
):
    """
    Добавить страну производителя.
    """
    return service.create(user_id=user.id, country_data=country_data)


@router.get('/{country_id}', response_model=Country)
def get_country(
        country_id: int,
        user: User = Depends(get_current_user),
        service: CountryService = Depends(),
):
    """
    Выдать страну производителя по ID.
    """
    return service.get_by_id(
        user_id=user.id,
        country_id=country_id)

@router.put('/{country_id}', response_model=Country)
def update_country(
        country_id: int,
        country_data: CountryUpdate,
        user: User = Depends(get_current_user),
        service: CountryService = Depends(),
):
    """
    Внести изменения в конкретную страну производителя.
    """
    return service.update(
        user_id=user.id,
        country_id=country_id,
        country_data=country_data,
    )

@router.delete('/{country_id}')
def delete_country(
        country_id: int,
        user: User = Depends(get_current_user),
        service: CountryService = Depends(),
):
    """
    Удалить страну производителя по ID.
    """
    service.delete(user_id=user.id, country_id=country_id, )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
