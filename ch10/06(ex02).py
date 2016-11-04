import win32com.client
instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
stockNum = instCpStockCode.GetCount()

for i in range(stockNum):
    if instCpStockCode.GetData(1, i) == 'NAVER':
        print(instCpStockCode.GetData(0,i))
        print(instCpStockCode.GetData(1,i))
        print(i)
