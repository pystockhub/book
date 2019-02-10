import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import mpl_finance

start = datetime.datetime(2016, 3, 1)
end = datetime.datetime(2016, 3, 31)

skhynix = web.DataReader("000660.KS", "yahoo", start, end)
#print(skhynix)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
mpl_finance.candlestick2_ohlc(ax, skhynix['Open'], skhynix['High'], skhynix['Low'], skhynix['Close'],
                         width=0.5, colorup='r', colordown='b')
plt.show()