import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2016, 2, 19)
end = datetime.datetime(2016, 3, 4)

gs = web.DataReader("078930.KS", "yahoo")

#plt.plot(gs['Adj Close'])
#plt.show()

plt.plot(gs.index, gs['Adj Close'])
plt.show()
