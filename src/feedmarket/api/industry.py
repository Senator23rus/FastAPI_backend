from typing import List

from fastapi import APIRouter
from fastapi import Depends

from ..models.industry import Industry
from ..services.industry import IndustryService

router = APIRouter(
    prefix='/industry',
    tags=['Индустрии'],
)

@router.get('/', response_model=List[Industry], )
def get_industry(service: IndustryService = Depends()):
    """

    Список всех индустрий
    """
    return service.get_list()
