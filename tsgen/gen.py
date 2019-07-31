import numpy as np
import pandas as pd

from .exceptions import InvalidValue


class TimeSerieGenerator:
    def __init__(
        self,
        date_start,
        date_end=pd.Timestamp.now(),
        freq="D",
        tz="UTC",
        low=0,
        high=100,
        ts_name=None,
    ):
        """
        Parameters
        ----------
        date_start : pandas.Timestamp, str
            The start date of range

        date_end : pandas.Timestamp, str, optional
            The end date of range

        freq : str, optional
            The frequency of Dates, e.g '5H'

        tz : str, optional
            Timezone of dates

        low : int, optional
            Lowest data to be generated

        high : int, optional
            Largest data to be generated

        ts_name : str, optional
            Name of timeseries
        """
        self.date_start = pd.to_datetime(date_start)
        self.date_end = pd.to_datetime(date_end)
        if self.date_start.tz is None:
            self.date_start = self.date_start.tz_localize(tz)
        else:
            self.date_start = self.date_start.tz_convert(tz)

        if self.date_end.tz is None:
            self.date_end = self.date_end.tz_localize(tz)
        else:
            self.date_end = self.date_end.tz_convert(tz)

        self.freq = freq
        self.tz = tz
        self.low = low
        self.high = high
        self.ts_name = ts_name

    def generate_df(self):
        """Return a pandas.DataFrame of random timeseries."""
        df = pd.DataFrame(
            index=pd.date_range(
                start=self.date_start, end=self.date_end, freq=self.freq, tz=self.tz
            )
        )
        df["value"] = np.random.randint(low=self.low, high=self.high, size=(len(df), 1))
        if self.ts_name is not None:
            df["ts_name"] = self.ts_name
        return df

    def export_df(self, df):
        """Create csv file of DataFrame

        Parameters
        ----------
        df : pandas.DataFrame
            DataFrame that will exported to csv
        """
        df.to_csv(
            f"{self.ts_name}_{pd.datetime.now().strftime('%y-%m-%d')}.csv",
            index_label="timestamp",
        )

    def generate(self):
        """Generate random pandas.DataFrame and export to csv file"""
        self.export_df(self.generate_df())
