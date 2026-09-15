from pandas import Index, DataFrame
from os import environ, makedirs
from json import load

def transform_weather (df_index : Index) -> None:
    weather_list = []
    for index in df_index:
        with open(f"{environ["BRONZE_PATH"]}/weather/{index}.json", "r", encoding="utf-8") as file:
            daily = load(file)["daily"]

        for date,\
            max_temp,\
            min_temp,\
            max_wind_speed, \
            max_wind_gusts, \
            weather_code, \
            max_precipitation_probability, \
            sum_precipitation \
        in list(zip(*daily.values())):

            weather_list.append({
                "city" : index,
                "date" : date,
                "max_temp" : max_temp,
                "min_temp" : min_temp,
                "max_wind_speed" : max_wind_speed,
                "max_wind_gusts" : max_wind_gusts,
                "weather_code" : weather_code,
                "max_precipitation_probability" : max_precipitation_probability,
                "sum_precipitation" : sum_precipitation
            })

    df = DataFrame(weather_list)

    makedirs(f"{environ["SILVER_PATH"]}/weather", exist_ok=True)
    df.to_csv(f"{environ["SILVER_PATH"]}/weather/cleaned.csv", index=False)
