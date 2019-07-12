import pandas as pd
import numpy as np
from .exceptions import InvalidValue


class TimeSerieGenerator:
    def __init__(self, date_start, date_end, freq, tz, low, high, ts_name):
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
        df = pd.DataFrame(
            index=pd.date_range(
                start=self.date_start, end=self.date_end, freq=self.freq, tz=self.tz
            )
        )
        df["value"] = np.random.randint(low=self.low, high=self.high, size=(len(df), 1))
        df["ts_name"] = self.ts_name
        return df

    def export_df(self, df):
        return df.to_csv(
            f"{self.ts_name}_{pd.datetime.now().strftime('%y-%m-%d')}.csv",
            index_label="timestamp",
        )

    def generate(self):
        return self.export_df(self.generate_df())
