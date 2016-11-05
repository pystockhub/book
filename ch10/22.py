import win32com.client

instCpTdUtil = win32com.client.Dispatch("CpTrade.CpTdUtil")
instCpTd0311 = win32com.client.Dispatch("CpTrade.CpTd0311")

instCpTdUtil.TradeInit()

accountNumber = instCpTdUtil.AccountNumber[0]
instCpTd0311.SetInputValue(0, 2)
instCpTd0311.SetInputValue(1, accountNumber)
instCpTd0311.SetInputValue(3, 'A003540')
instCpTd0311.SetInputValue(4, 10)
instCpTd0311.SetInputValue(5, 13000)
instCpTd0311.BlockRequest()
