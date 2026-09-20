from sqlalchemy import Table, Column, String, Date, ForeignKey, Float, Integer
from ..metadata import metadata

weather_table = Table(
    "weather",
    metadata,
    Column("city", String, ForeignKey("cities.name"), primary_key=True),
    Column("date", Date, primary_key=True),
    Column("max_temp", Float, nullable=False),
    Column("min_temp", Float, nullable=False),
    Column("max_wind_speed", Float, nullable=False),
    Column("max_wind_gusts", Float, nullable=False),
    Column("weather_code", Integer, nullable=False),
    Column("max_precipitation_probability", Float, nullable=False),
    Column("sum_precipitation", Float, nullable=False),
    Column("risk_score", Integer, nullable=False),
    Column("avg_temp", Integer, nullable=False),
    Column("temp_category", String, nullable=False),
    Column("wind_category", String, nullable=False),
    Column("precipitation_category", String, nullable=False)
)