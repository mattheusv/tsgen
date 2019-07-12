import pandas as pd
import numpy as np
import os.path
from unittest import TestCase
from tsgen.gen import TimeSerieGenerator


class TimeSerieGeneratorTestCase(TestCase):
    def test_generate_df_freq(self):
        ts_gen = TimeSerieGenerator(
            date_start="1990-01-01",
            date_end="1990-01-02",
            freq="D",
            tz="UTC",
            low=0,
            high=100,
            ts_name="ts.test",
        )
        df = ts_gen.generate_df()
        self.assertEqual(len(df), 2)

    def test_export_df(self):
        ts_gen = TimeSerieGenerator(
            date_start="1990-01-01",
            date_end="1990-01-02",
            freq="D",
            tz="UTC",
            low=0,
            high=100,
            ts_name="ts.test",
        )
        df = ts_gen.generate_df()
        ts_gen.export_df(df)
        self.assertTrue(
            os.path.exists(
                f"{ts_gen.ts_name}_{pd.datetime.now().strftime('%y-%m-%d')}.csv"
            )
        )
