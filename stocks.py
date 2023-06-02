import requests

api_key = "X6Z9ATCYSWYJJG4I"

from alpha_vantage.timeseries import TimeSeries

ts= TimeSeries(key= api_key,output_format='pandas')
data=ts.get_daily_adjusted('AAPL')

print(data[0])
