from sqlalchemy.orm import sessionmaker
from databases import Database
from sqlalchemy import create_engine, MetaData
# from .settings import DATABASE_URL
from .settings import settings

engine = create_engine(settings.database_url)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
