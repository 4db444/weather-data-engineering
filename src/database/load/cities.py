from pandas import DataFrame
from ..connection import engine
from ..queries import insert_city

def load_cities_to_db (df : DataFrame):
    with engine.connect() as conn:
        for city in df.itertuples():
            insert_city(conn, city)
