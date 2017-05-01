import win32com.client
instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
for i in range(0, 10):
    print(instCpStockCode.GetData(1,i))

