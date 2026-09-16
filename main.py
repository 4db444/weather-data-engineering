from src import get_weather, transform_weather, add_features
import pandas as pd
from dotenv import load_dotenv
from os import environ

def main() -> None:
    load_dotenv()

    df = pd.read_csv(f"{environ["SILVER_PATH"]}/weather/cleaned.csv", index_col="city")

    # get_weather(df)

    # transform_weather(df.index)

    add_features(df)
    print(df)

if __name__ == "__main__":
    main()