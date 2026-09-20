from .connection import engine
from .metadata import metadata
from .tables import cities_table, weather_table     


def init_db():
    
    metadata.create_all(engine)

