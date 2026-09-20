from pandas import DataFrame
from ..connection import engine
from ..queries import insert_weather

def load_weather_to_db (df : DataFrame):
    with engine.connect() as conn:
        for city in df.itertuples():
            insert_weather(conn, city)