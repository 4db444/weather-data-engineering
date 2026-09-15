from src import get_weather
import pandas as pd
from dotenv import load_dotenv
from os import environ

load_dotenv()

df = pd.read_csv(f"{environ["BRONZE_PATH"]}/cities/ma.csv")

get_weather(df)