from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

url = 'postgresql://postgres:3EVDj2wZ@localhost:5432/DB'


def get_engine(url):
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, echo=True)
    return engine


engine = get_engine(url)

