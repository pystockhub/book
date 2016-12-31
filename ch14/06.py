import pandas_datareader.data as web
import datetime
from zipline.api import order_target, record, symbol
from zipline.algorithm import TradingAlgorithm
from zipline.api import set_commission, commission
import matplotlib.pyplot as plt

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2016, 1, 31)
data = web.DataReader("078930.KS", "yahoo", start, end)

data = data[['Adj Close']]
data.columns = ['GS']
data = data.tz_localize('UTC')

def initialize(context):
    context.i = 0
    context.sym = symbol('GS')
    set_commission(commission.PerDollar(cost=0.00165))

def handle_data(context, data):
    order_target(context.sym, 1)

algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
result = algo.run(data)

print(result[['starting_cash', 'ending_cash', 'ending_value']])
#print(result.head())

