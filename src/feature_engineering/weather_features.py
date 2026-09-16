from pandas import Series, DataFrame, cut
from os import makedirs, environ

def _calculate_risk_score(row: Series) -> int:
    score = 0

    # For max temperature.
    if row["max_temp"] > 35 : score += 40
    elif row["max_temp"] > 30 : score += 20

    # For min temperature.
    if row["min_temp"] < 5 : score += 30
    elif row["min_temp"] < 10 : score += 15

    # For precipitation.
    if row["sum_precipitation"] > 10 : score += 30
    elif row["sum_precipitation"] > 0 : score += 15

    return score

def _add_risk_score(df : DataFrame) -> None:

    df["risk_score"] = df.apply(
        _calculate_risk_score,
        axis=1
    )
    df["avg_temp"] = (df["min_temp"] + df["max_temp"]) / 2

def _add_avg_temp(df : DataFrame) -> None:
    df["avg_temp"] = (df["min_temp"] + df["max_temp"]) / 2

def _add_temp_category(df : DataFrame) -> None:
    df["temp_category"] = cut(
        df["avg_temp"],
        bins=[-float("inf"), 0, 10, 18, 25, 30, 35, 40, float("inf")],
        labels=[
            "Freezing",
            "Cold", 
            "Cool", 
            "Mild", 
            "Warm", 
            "Hot", 
            "Very Hote", 
            "Extreme Heat"
        ]
    )

def _add_precipitation_category(df : DataFrame) -> None:
    df["precipitation_category"] = cut(
        df["sum_precipitation"],
        bins=[-float("inf"), 0.1, 5, 10, 25, 50, 100, float("inf")],
        labels=[
            "Sunny",
            "Very Light",
            "Light",
            "Moderate",
            "Heavy",
            "Very Heavy",
            "Extreme"
        ]
    )

def _add_wind_category(df : DataFrame) -> None:
    df["wind_category"] = cut(
        df["max_wind_speed"],
        bins=[-float("inf"), 5, 15, 25, 40, 55, 75, float("inf")],
        labels=[
            "Calm",
            "Light",
            "Moderate",
            "Breezy",
            "Strong",
            "Very Strong",
            "Extreme"
        ]
    )


# The fucntion that inserts all the features at ones:
def add_features(df : DataFrame) -> None:
    _add_risk_score(df)
    _add_avg_temp(df)
    _add_temp_category(df)
    _add_wind_category(df)
    _add_precipitation_category(df)

    makedirs(f"{environ["GOLD_PATH"]}/weather", exist_ok=True)
    df.to_csv(f"{environ["GOLD_PATH"]}/weather/gold.csv")