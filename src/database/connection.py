from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from urllib.parse import quote
from os import environ


_db_driver = environ["DB_DRIVER"]
_db_name = environ["DB_NAME"]
_db_password = environ["DB_PASSWORD"]
_db_host = environ["DB_HOST"]
_db_port = environ["DB_PORT"]
_db_user = environ["DB_USER"]

db_url = f"{_db_driver}://{_db_user}:{quote(_db_password)}@{_db_host}:{_db_port}/{_db_name}"

if not database_exists(db_url):
    create_database(db_url)

engine = create_engine(db_url)
