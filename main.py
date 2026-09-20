from dotenv import load_dotenv
load_dotenv()
from src import get_weather, transform_weather, add_features, transform_cities, init_db, load_cities_to_db, load_weather_to_db
import pandas as pd
from os import environ



def main() -> None:
    init_db()

    # Bronze Stage
    cities_df = pd.read_csv(f"{environ["BRONZE_PATH"]}/cities/ma.csv")
    cities_df = get_weather(cities_df)

    # Silver stage
    weather_df = transform_weather(cities_df.index)
    transform_cities(cities_df)

    # Gold Stage
    weather_df = add_features(weather_df)
    load_cities_to_db(cities_df)
    load_weather_to_db(weather_df)

if __name__ == "__main__":
    main()