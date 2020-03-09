"""Download the JHU CSSE time series and reshape it."""
import pandas as pd

BASE = (
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/"
    "csse_covid_19_data/csse_covid_19_time_series/"
)
CONFIRMED = BASE + "time_series_covid19_confirmed_global.csv"
DEATHS = BASE + "time_series_covid19_deaths_global.csv"


def load(url: str) -> pd.DataFrame:
    df = pd.read_csv(url)
    df = df.drop(columns=["Province/State", "Lat", "Long"])
    df = df.groupby("Country/Region").sum().T
    df.index = pd.to_datetime(df.index)
    return df


def confirmed() -> pd.DataFrame:
    return load(CONFIRMED)


def deaths() -> pd.DataFrame:
    return load(DEATHS)
