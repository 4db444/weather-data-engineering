from sqlalchemy import Table, Column, String, Float
from ..metadata import metadata


cities_table = Table(
    "cities",
    metadata,
    Column("name", String, primary_key=True),
    Column("lat", Float, nullable=False),
    Column("lng", Float, nullable=False),
    Column("country", String, nullable=False),
    Column("iso2", String, nullable=False),
    Column("admin_name", String, nullable=False)
)