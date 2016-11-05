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

class XAQueryEventHandlerT8430:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT8430.query_state = 1


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
# T8430
# ----------------------------------------------------------------------------
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

