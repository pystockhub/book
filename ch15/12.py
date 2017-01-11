import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import matplotlib.finance as matfin

start = datetime.datetime(2016, 3, 1)
end = datetime.datetime(2016, 3, 31)

skhynix = web.DataReader("000660.KS", "yahoo", start, end)
skhynix = skhynix[skhynix['Volume'] > 0]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

matfin.candlestick2_ohlc(ax, skhynix['Open'], skhynix['High'], skhynix['Low'], skhynix['Close'],
                         width=0.5, colorup='r', colordown='b')
plt.show()