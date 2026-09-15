from pandas import DataFrame
from os import environ, makedirs


def transform_cities (df : DataFrame) -> None:

    df = df.drop(columns=["capital", "population", "population_proper"])

    makedirs(f"{environ["SILVER_PATH"]}/cities", exist_ok=True)

    df.to_csv(f"{environ["SILVER_PATH"]}/cities/cleaned.csv")