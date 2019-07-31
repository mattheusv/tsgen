# tsgen [![Build Status](https://travis-ci.org/msalcantara/tsgen.svg?branch=master)](https://travis-ci.org/msalcantara/tsgen) [![Coverage Status](https://coveralls.io/repos/github/msalcantara/tsgen/badge.svg?branch=master)](https://coveralls.io/github/msalcantara/tsgen?branch=master)
 TimeSeries generator

## Instalation
 - `$ git clone https://github.com/msalcantara/tsgen`
 - `$ python -m venv venv`
 - `$ source venv/bin/activate`
 - `$ python setup.py install`
 - `$ tsgen --help`

## Usage
 - `$ tsgen -s 2019-01-01 cpu.idle`
 - `$ head cpu.idle_19-07-11.csv`
 ```csv
 timestamp,value,ts_name
 2019-01-01 00:00:00+00:00,61,cpu.idle
 2019-01-02 00:00:00+00:00,0,cpu.idle
 2019-01-03 00:00:00+00:00,27,cpu.idle
 2019-01-04 00:00:00+00:00,33,cpu.idle
 2019-01-05 00:00:00+00:00,9,cpu.idle
 2019-01-06 00:00:00+00:00,63,cpu.idle
 2019-01-07 00:00:00+00:00,63,cpu.idle
 2019-01-08 00:00:00+00:00,24,cpu.idle
 2019-01-09 00:00:00+00:00,12,cpu.idle
 ```
 - `$ tail cpu.idle_19-07-11.cs`
 ```csv
 2019-07-02 00:00:00+00:00,68,cpu.idle
 2019-07-03 00:00:00+00:00,94,cpu.idle
 2019-07-04 00:00:00+00:00,53,cpu.idle
 2019-07-05 00:00:00+00:00,53,cpu.idle
 2019-07-06 00:00:00+00:00,35,cpu.idle
 2019-07-07 00:00:00+00:00,64,cpu.idle
 2019-07-08 00:00:00+00:00,28,cpu.idle
 2019-07-09 00:00:00+00:00,51,cpu.idle
 2019-07-10 00:00:00+00:00,38,cpu.idle
 2019-07-11 00:00:00+00:00,98,cpu.idle
 ```
 #### With frequency in minute by minute?
  - `$ tsgen -s 2019-01-01 -f min cpu.idle`
  - `$ head cpu.idle_19-07-11.csv`
  ```csv
  timestamp,value,ts_name
  2019-01-01 00:00:00+00:00,76,cpu.idle
  2019-01-01 00:01:00+00:00,33,cpu.idle
  2019-01-01 00:02:00+00:00,98,cpu.idle
  2019-01-01 00:03:00+00:00,87,cpu.idle
  2019-01-01 00:04:00+00:00,53,cpu.idle
  2019-01-01 00:05:00+00:00,6,cpu.idle
  2019-01-01 00:06:00+00:00,25,cpu.idle
  2019-01-01 00:07:00+00:00,15,cpu.idle
  2019-01-01 00:08:00+00:00,70,cpu.idle
  ```
 ### For more commands
 ```
 Usage: tsgen [OPTIONS] TIMESERIE_NAME

Options:
  -s, --date-start TIMESTAMP  Date start of timeseries data [YYYY-MM-
                              DD]/[YYYY-MM-DD HH:MM:SS]  [required]
  -e, --date-end TIMESTAMP    Date end of timeseries data [YYYY-MM-DD]/[YYYY-
                              MM-DD HH:MM:SS]  [default: now]
  -f, --freq TEXT             Frequency of dates, e.g. '5H'  [default: D]
  --tz TEXT                   Timezone of dates  [default: UTC]
  --low INTEGER               Lowest data to be generated  [default: 0]
  --high INTEGER              Largest data to be generated
  --version                   Show version
  --help                      Show this message and exit.
 ```
 ### Frequency Alias
 - B	business day frequency
 - C	custom business day frequency
 - D	calendar day frequency
 - W	weekly frequency
 - M	month end frequency
 - SM	semi-month end frequency (15th and end of month)
 - BM	business month end frequency
 - CBM	custom business month end frequency
 - MS	month start frequency
 - SMS	semi-month start frequency (1st and 15th)
 - BMS	business month start frequency
 - CBMS	custom business month start frequency
 - Q	quarter end frequency
 - BQ	business quarter end frequency
 - QS	quarter start frequency
 - BQS	business quarter start frequency
 - A, Y	year end frequency
 - BA, BY	business year end frequency
 - AS, YS	year start frequency
 - BAS, BYS	business year start frequency
 - BH	business hour frequency
 - H	hourly frequency
 - T, min	minutely frequency
 - S	secondly frequency
 - L, ms	milliseconds
 - U, us	microseconds
 - N	nanoseconds

 ## Use with dependencie in project
 ```python
 from tsgen.gen import TimeSerieGenerator
 ts = TimeSerieGenerator('1990-01-01')
 df = ts.generate_df()
 print(df.head())
 ```

## License
 [MIT](https://raw.githubusercontent.com/msalcantara/tsgen/master/LICENSE) license.
