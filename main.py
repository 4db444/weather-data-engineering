from src import get_weather, transform_weather
import pandas as pd
from dotenv import load_dotenv
from os import environ

load_dotenv()

df = pd.read_csv(f"{environ["BRONZE_PATH"]}/cities/ma.csv", index_col="city")

# get_weather(df)

transform_weather(df.index)