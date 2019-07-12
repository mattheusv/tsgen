import sys
import click
import pandas as pd
import numpy as np
from pytz.exceptions import UnknownTimeZoneError
from os import path
from .gen import TimeSerieGenerator


def version():
    try:
        version_file = path.join(path.abspath(path.dirname(__file__)), "VERSION")
        with open(version_file) as f:
            return f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(
            "error: tsgen not installed correctly\n Try running python setup.py install"
        )


@click.command()
@click.option(
    "--date-start",
    required=True,
    type=pd.Timestamp,
    help="Date start of timeseries data [YYYY-MM-DD]/[YYYY-MM-DD HH:MM:SS]",
)
@click.option(
    "--date-end",
    default=None,
    type=pd.Timestamp,
    help="Date end of timeseries data [YYYY-MM-DD]/[YYYY-MM-DD HH:MM:SS]  [default: now]",
)
@click.option(
    "--freq", default="D", show_default=True, help="Frequency of dates, e.g. '5H'"
)
@click.option(
    "--tz", type=str, default="UTC", show_default=True, help="Timezone of dates"
)
@click.option("--low", default=0, show_default=True, help="Lowest data to be generated")
@click.option(
    "--high", default=None, required=True, help="Largest data to be generated"
)
@click.option("--version", type=bool, default=False, is_flag=True, help="Show version")
@click.argument("timeserie-name", required=True)
def main(date_end, **kwargs):
    try:
        if date_end is None:
            date_end = pd.Timestamp.now(tz=kwargs["tz"])
        ts_gen = TimeSerieGenerator(
            kwargs["date_start"],
            date_end,
            kwargs["freq"],
            kwargs["tz"],
            kwargs["low"],
            kwargs["high"],
            kwargs["timeserie_name"],
        ).generate()
    except UnknownTimeZoneError as e:
        print(f"Unknown TimeZone Error: {e}")


if __name__ == "__main__":
    main()
