import pandas_datareader.data as web
import datetime

start = datetime.datetime(2016, 2, 19)
end = datetime.datetime(2016, 3, 4)

gs = web.DataReader("078930.KS", "yahoo", start, end)
print(gs)