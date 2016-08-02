import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QAxContainer import *
import time
import pandas as pd
import sqlite3

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

        self.connect(self, SIGNAL("OnEventConnect(int)"), self.OnEventConnect)
        self.connect(self, SIGNAL("OnReceiveTrData(QString, QString, QString, QString, QString, int, QString, \
                                   QString, QString)"), self.OnReceiveTrData)

    def CommConnect(self):
        self.dynamicCall("CommConnect()")

        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def OnEventConnect(self, errCode):
        if errCode == 0:
            print("connected")
        else:
            print("disconnected")

        self.login_event_loop.exit()

    def SetInputValue(self, sID, sValue):
        self.dynamicCall("SetInputValue(QString, QString)", sID, sValue)

    def CommRqData(self, sRQName, sTRCode, nPrevNext, sScreenNo):
        self.dynamicCall("CommRqData(QString, QString, int, QString)", sRQName, sTRCode, nPrevNext, sScreenNo)

        self.tr_event_loop = QEventLoop()
        self.tr_event_loop.exec_()

    def CommGetData(self, sJongmokCode, sRealType, sFieldName, nIndex, sInnerFiledName):
        data = self.dynamicCall("CommGetData(QString, QString, QString, int, QString)", sJongmokCode, sRealType,
                                sFieldName, nIndex, sInnerFiledName)
        return data.strip()

    def OnReceiveTrData(self, ScrNo, RQName, TrCode, RecordName, PrevNext, DataLength, ErrorCode, Message, SplmMsg):
        self.prev_next = PrevNext

        if RQName == "opt10081_req":
            cnt = self.GetRepeatCnt(TrCode, RQName)

            for i in range(cnt):
                date = self.CommGetData(TrCode, "", RQName, i, "일자")
                open = self.CommGetData(TrCode, "", RQName, i, "시가")
                high = self.CommGetData(TrCode, "", RQName, i, "고가")
                low  = self.CommGetData(TrCode, "", RQName, i, "저가")
                close  = self.CommGetData(TrCode, "", RQName, i, "현재가")

                self.ohlc['date'].append(date)
                self.ohlc['open'].append(int(open))
                self.ohlc['high'].append(int(high))
                self.ohlc['low'].append(int(low))
                self.ohlc['close'].append(int(close))

        self.tr_event_loop.exit()

    def GetRepeatCnt(self, sTrCode, sRecordName):
        ret = self.dynamicCall("GetRepeatCnt(QString, QString)", sTrCode, sRecordName)
        return ret

    def GetCodeListByMarket(self, sMarket):
        cmd = 'GetCodeListByMarket("%s")' % sMarket
        ret = self.dynamicCall(cmd)
        item_codes = ret.split(';')
        return item_codes

    def GetMasterCodeName(self, strCode):
        cmd = 'GetMasterCodeName("%s")' % strCode
        ret = self.dynamicCall(cmd)
        return ret

    def GetConnectState(self):
        ret = self.dynamicCall("GetConnectState()")
        return ret

    def InitOHLCRawData(self):
        self.ohlc = {'date': [], 'open': [], 'high': [], 'low': [], 'close': []}

if __name__ == "__main__":
    app = QApplication(sys.argv)

    kiwoom = Kiwoom()
    kiwoom.CommConnect()
    kiwoom.InitOHLCRawData()

    # TR
    kiwoom.SetInputValue("종목코드", "039490")
    kiwoom.SetInputValue("기준일자", "20160624")
    kiwoom.SetInputValue("수정주가구분", 1)
    kiwoom.CommRqData("opt10081_req", "opt10081", 0, "0101")

    while kiwoom.prev_next == '2':
        time.sleep(0.2)
        kiwoom.SetInputValue("종목코드", "039490")
        kiwoom.SetInputValue("기준일자", "20160624")
        kiwoom.SetInputValue("수정주가구분", 1)
        kiwoom.CommRqData("opt10081_req", "opt10081", 2, "0101")

    df = pd.DataFrame(kiwoom.ohlc, columns=['open', 'high', 'low', 'close'], index=kiwoom.ohlc['date'])
    print(df.head())
    con = sqlite3.connect("c:/Users/Jason/stock.db")
    df.to_sql('039490', con, if_exists='replace')
