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

class XAQueryEventHandlerT1102:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT1102.query_state = 1

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
# t1102
# ----------------------------------------------------------------------------
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
