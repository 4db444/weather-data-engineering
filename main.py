from src import get_weather, transform_weather, add_features, transform_cities
import pandas as pd
from dotenv import load_dotenv
from os import environ

def main() -> None:
    load_dotenv()

    # Bronze Stage
    cities_df = pd.read_csv(f"{environ["BRONZE_PATH"]}/cities/ma.csv")
    cities_df = get_weather(cities_df.head(20))

    # Silver stage
    weather_df = transform_weather(cities_df.index)
    transform_cities(cities_df)

    # Gold Stage
    weather_df = add_features(weather_df)

if __name__ == "__main__":
    main()