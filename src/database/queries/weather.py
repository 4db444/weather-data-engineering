from ..tables import weather_table
from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError

def insert_weather(conn, row) -> None:

    try:
        stmt = insert(weather_table).values(
            city=row.Index[0],
            date=row.Index[1],
            max_temp=row.max_temp,
            min_temp=row.min_temp,
            max_wind_speed=row.max_wind_speed,
            max_wind_gusts=row.max_wind_gusts,
            weather_code=row.weather_code,
            max_precipitation_probability=row.max_precipitation_probability,
            sum_precipitation=row.sum_precipitation,
            risk_score=row.risk_score,
            avg_temp=row.avg_temp,
            temp_category=row.temp_category,
            wind_category=row.wind_category,
            precipitation_category=row.precipitation_category
        )

        conn.execute(stmt)

        conn.commit()

    except Exception as e:
        if isinstance(e, IntegrityError):
            print(f"row '{row.Index[0]}'@'{row.Index[1]}', is already exists !")

        conn.rollback()