from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError
from ..tables import cities_table

def insert_city(conn, row) -> None:
    try:

        stmt = insert(cities_table).values(
            name=row.Index,
            lat=row.lat,
            lng=row.lng,
            country=row.country,
            iso2=row.iso2,
            admin_name=row.admin_name,
        )

        conn.execute(stmt)

        conn.commit()
    except Exception as e:
        if isinstance(e, IntegrityError): 
            print(f"row '{row.Index}', already exists !")
            
        conn.rollback()