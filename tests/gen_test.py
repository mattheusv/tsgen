import pandas as pd
import numpy as np
from unittest import TestCase
from tsgen.gen import TimeSerieGenerator
from tsgen.exceptions import InvalidValue


class TimeSerieGeneratorTestCase(TestCase):
    def test_timeserie_generator_valid(self):
        try:
            TimeSerieGenerator(
                date_start="01-01-1990",
                date_end=pd.Timestamp.now(),
                freq="D",
                tz="UTC",
                low=0,
                high=100,
                dtype=np.int,
                ts_name="ts.test",
            )
        except InvalidValue as e:
            self.failIf("unknown timeserie generator invalid value exception", e)

    def test_generate_df(self):
        try:
            ts_gen = TimeSerieGenerator(
                date_start="1990-01-01",
                date_end=pd.Timestamp.now(),
                freq="D",
                tz="UTC",
                low=0,
                high=100,
                dtype=np.int,
                ts_name="ts.test",
            )
            df = ts_gen.generate_df()
            print(df.head())
        except Exception as e:
            self.failIf("unknown exception", e)
