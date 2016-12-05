import pandas_datareader.data as web
import pandas as pd

gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")
gs['Volume'] != 0
ma5 = gs['Adj Close'].rolling(window=5).mean()
print(type(ma5))
print(ma5)