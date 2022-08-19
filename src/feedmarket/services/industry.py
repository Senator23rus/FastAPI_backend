from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import tables
from ..database import get_session
from ..tables import Industry


class IndustryService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self, ) -> list[Industry]:
        query = self.session.query(tables.Industry)
        industry = query.all()
        return industry
