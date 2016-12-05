import pandas_datareader.data as web
import pandas as pd

gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")
new_gs = gs[gs['Volume'] !=0]

#ma5 = gs['Adj Close'].rolling(window=5).mean()
#print(ma5.tail(10))

#ma5 = gs['Adj Close'].rolling(window=5).mean()
#new_gs['MA5'] = ma5
#print(new_gs)

# m20, ma60, ma120
ma20 = gs['Adj Close'].rolling(window=20).mean()
ma60 = gs['Adj Close'].rolling(window=60).mean()
ma120 = gs['Adj Close'].rolling(window=120).mean()

new_gs['MA20'] = ma20
new_gs['MA60'] = ma60
new_gs['MA120'] = ma120

print(new_gs.tail(10))
