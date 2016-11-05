import win32com.client
import pythoncom

class XAQueryEventHandlerT8430:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT8430.query_state = 1

instXAQueryT8430 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandlerT8430)
instXAQueryT8430.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t8430.res"

instXAQueryT8430.SetFieldData("t8430InBlock", "gubun", 0, 1)
instXAQueryT8430.Request(0)

while XAQueryEventHandlerT8430.query_state == 0:
    pythoncom.PumpWaitingMessages()

count = instXAQueryT8430.GetBlockCount("t8430OutBlock")
for i in range(5):
    hname = instXAQueryT8430.GetFieldData("t8430OutBlock", "hname", i)
    shcode = instXAQueryT8430.GetFieldData("t8430OutBlock", "shcode", i)
    expcode = instXAQueryT8430.GetFieldData("t8430OutBlock", "expcode", i)
    etfgubun = instXAQueryT8430.GetFieldData("t8430OutBlock", "etfgubun", i)
    print(i, hname, shcode, expcode, etfgubun)
