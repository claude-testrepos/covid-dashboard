import argparse

import matplotlib.pyplot as plt

import data

DEFAULT = ["Italy", "Spain", "US", "Canada", "Korea, South"]


def since_n_cases(df, n=100):
    """Align each country's curve on the day it passed n cases."""
    out = {}
    for country in df.columns:
        s = df[country]
        s = s[s >= n].reset_index(drop=True)
        out[country] = s
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("countries", nargs="*", default=DEFAULT)
    p.add_argument("--deaths", action="store_true")
    p.add_argument("--log", action="store_true", help="log scale")
    p.add_argument("--daily", action="store_true", help="new cases per day (7-day avg)")
    p.add_argument("--save", help="write png instead of showing")
    args = p.parse_args()

    df = data.deaths() if args.deaths else data.confirmed()
    df = df[args.countries]
    if args.daily:
        df = df.diff().rolling(7).mean()
        df.plot(figsize=(10, 6))
        plt.xlabel("date")
    else:
        aligned = since_n_cases(df, 10 if args.deaths else 100)
        plt.figure(figsize=(10, 6))
        for country, s in aligned.items():
            plt.plot(s.index, s.values, label=country)
        plt.xlabel("days since 100th case")
        plt.legend()
    if args.log:
        plt.yscale("log")
    plt.title("COVID-19 " + ("deaths" if args.deaths else "confirmed cases"))
    plt.grid(alpha=.3)
    if args.save:
        plt.savefig(args.save, dpi=150, bbox_inches="tight")
    else:
        plt.show()


if __name__ == "__main__":
    main()
