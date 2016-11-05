import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
industryCodeList = instCpCodeMgr.GetIndustryList()

for industryCode in industryCodeList:
    print(industryCode, instCpCodeMgr.GetIndustryName(industryCode))
