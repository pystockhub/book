import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
tarketCodeList = instCpCodeMgr.GetGroupCodeList(5)

for code in tarketCodeList:
    print(code, instCpCodeMgr.CodeToName(code))
