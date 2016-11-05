import win32com.client
import pythoncom

class XAQueryEventHandlerT1102:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT1102.query_state = 1

instXAQueryT1102 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandlerT1102)
instXAQueryT1102.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t1102.res"
instXAQueryT1102.SetFieldData("t1102InBlock", "shcode", 0, "078020")
instXAQueryT1102.Request(0)

while XAQueryEventHandlerT1102.query_state == 0:
    pythoncom.PumpWaitingMessages()

name = instXAQueryT1102.GetFieldData("t1102OutBlock", "hname", 0)
price = instXAQueryT1102.GetFieldData("t1102OutBlock", "price", 0)
print(name)
print(price)
