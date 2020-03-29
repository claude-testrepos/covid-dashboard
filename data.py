"""Download the JHU CSSE time series and reshape it."""
import time
import urllib.request
from pathlib import Path

import pandas as pd

BASE = (
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/"
    "csse_covid_19_data/csse_covid_19_time_series/"
)
CONFIRMED = BASE + "time_series_covid19_confirmed_global.csv"
DEATHS = BASE + "time_series_covid19_deaths_global.csv"


CACHE = Path(".cache")


def cached(url: str, max_age: int = 6 * 3600) -> Path:
    """JHU updates once a day, no need to download 2MB on every run."""
    CACHE.mkdir(exist_ok=True)
    path = CACHE / url.rsplit("/", 1)[1]
    if not path.exists() or time.time() - path.stat().st_mtime > max_age:
        urllib.request.urlretrieve(url, path)
    return path


def load(url: str) -> pd.DataFrame:
    df = pd.read_csv(cached(url))
    df = df.drop(columns=["Province/State", "Lat", "Long"])
    df = df.groupby("Country/Region").sum().T
    df.index = pd.to_datetime(df.index)
    return df


def confirmed() -> pd.DataFrame:
    return load(CONFIRMED)


def deaths() -> pd.DataFrame:
    return load(DEATHS)
