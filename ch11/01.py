class XASessionEventHandler:
    login_state = 0

    def OnLogin(self, code, msg):
        if code == "0000":
            print("로그인 성공")
            XASessionEventHandler.login_state = 1
        else:
            print("로그인 실패")

