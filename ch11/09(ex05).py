import win32com.client
import pythoncom

class XASessionEventHandler:
    login_state = 0

    def OnLogin(self, code, msg):
        if code == "0000":
            print("로그인 성공")
            XASessionEventHandler.login_state = 1
        else:
            print("로그인 실패")

class XAQueryEventHandlerT8413:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT8413.query_state = 1


# ----------------------------------------------------------------------------
# login
# ----------------------------------------------------------------------------
id = "id"
passwd = "passwd"
cert_passwd = "cert"

instXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEventHandler)
instXASession.ConnectServer("hts.ebestsec.co.kr", 20001)
instXASession.Login(id, passwd, cert_passwd, 0, 0)

while XASessionEventHandler.login_state == 0:
    pythoncom.PumpWaitingMessages()


# ----------------------------------------------------------------------------
# T8413
# ----------------------------------------------------------------------------
instXAQueryT8413 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandlerT8413)
instXAQueryT8413.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t8413.res"

instXAQueryT8413.SetFieldData("t8413InBlock", "shcode", 0, "078020")
instXAQueryT8413.SetFieldData("t8413InBlock", "gubun", 0, "2")
instXAQueryT8413.SetFieldData("t8413InBlock", "sdate", 0, "20160111")
instXAQueryT8413.SetFieldData("t8413InBlock", "edate", 0, "20160122")
instXAQueryT8413.SetFieldData("t8413InBlock", "comp_yn", 0, "N")

instXAQueryT8413.Request(0)

while XAQueryEventHandlerT8413.query_state == 0:
    pythoncom.PumpWaitingMessages()

count = instXAQueryT8413.GetBlockCount("t8413OutBlock1")
for i in range(count):
    date = instXAQueryT8413.GetFieldData("t8413OutBlock1", "date", i)
    open = instXAQueryT8413.GetFieldData("t8413OutBlock1", "open", i)
    high = instXAQueryT8413.GetFieldData("t8413OutBlock1", "high", i)
    low = instXAQueryT8413.GetFieldData("t8413OutBlock1", "low", i)
    close = instXAQueryT8413.GetFieldData("t8413OutBlock1", "close", i)
    print(date, open, high, low, close)


