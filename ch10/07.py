import win32com.client
instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")

naverCode = instCpStockCode.NameToCode('NAVER')
naverIndex = instCpStockCode.CodeToIndex(naverCode)
print(naverCode)
print(naverIndex)
