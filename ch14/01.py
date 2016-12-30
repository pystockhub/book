import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

# data
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 3, 19)
data = web.DataReader("AAPL", "yahoo", start, end)

plt.plot(data.index, data['Adj Close'])
plt.show()