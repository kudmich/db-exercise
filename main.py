import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

# engine = create_engine('postgresql://postgres:3EVDj2wZ@localhost:5432/DB', echo=True)
url = 'postgresql://postgres:3EVDj2wZ@localhost:5432/DB5'


def get_engine(url):
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, echo=True)
    return engine


engine = get_engine(url)

