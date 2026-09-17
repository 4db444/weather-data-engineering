import requests
from pandas import DataFrame
from json import dump
from os import environ, makedirs

def get_weather(df : DataFrame) -> DataFrame:
    try:
        url = environ["API_URL"]

        for row in df.itertuples(index=False):
            params = {
                "latitude" : str(row.lat),
                "longitude" : str(row.lng)
            }

            res = requests.get(url, params=params)

            print(f"Fetched {row.city} Data")

            with open(f"{environ["BRONZE_PATH"]}/weather/{row.city}.json", "w", encoding="utf-8") as file:
                dump(res.json(), file)

    except Exception as e:
        print(e)

    return df.set_index("city")


