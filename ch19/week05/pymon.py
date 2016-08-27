import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QAxContainer import *
import Kiwoom
import pandas as pd
import datetime
import time

MARKET_KOSPI   = 0
MARKET_KOSDAK  = 10

class PyMon:
    def __init__(self):
        self.kiwoom = Kiwoom.Kiwoom()
        self.kiwoom.CommConnect()
        self.get_code_list()

    def get_code_list(self):
        self.kospi_codes = self.kiwoom.GetCodeListByMarket(MARKET_KOSPI)
        self.kosdak_codes = self.kiwoom.GetCodeListByMarket(MARKET_KOSDAK)

    def get_ohlcv(self, code, start_date):
        # Init data structure
        self.kiwoom.InitOHLCRawData()

        # Request TR and get data
        self.kiwoom.SetInputValue("종목코드", code)
        self.kiwoom.SetInputValue("기준일자", start_date)
        self.kiwoom.SetInputValue("수정주가구분", 1)
        self.kiwoom.CommRqData("opt10081_req", "opt10081", 0, "0101")
        time.sleep(0.2)

        # DataFrame
        df = pd.DataFrame(self.kiwoom.ohlcv, columns=['open', 'high', 'low', 'close', 'volume'],
                          index=self.kiwoom.ohlcv['date'])
        return df

    def check_speedy_rising_volumn(self, code):
        today = datetime.datetime.today().strftime("%Y%m%d")
        df = self.get_ohlcv(code, today)
        volumes = df['volume']

        sum_vol20 = 0
        avg_vol20 = 0

        # Check small trading days
        if len(volumes) < 21:
            return False

        # Accumulation
        for i, vol in enumerate(volumes):
            if i == 0:
                today_vol = vol
            elif i >= 1 and i <= 20:
                sum_vol20 += vol
            elif i >= 21:
                break

        #  Average and decision
        avg_vol20 = sum_vol20 / 20;
        if today_vol > avg_vol20 * 10:
            return True
        else:
            return False

    def update_buy_list(self, buy_list):
        f = open("buy_list.txt", "wt")
        for code in buy_list:
            f.writelines("매수;%s;시장가;10;0;매수전\n" % (code))
        f.close()

    def run(self):
        buy_list = []

        for code in self.kospi_codes:
            if self.check_speedy_rising_volumn(code):
                buy_list.append(code)

        for code in self.kosdak_codes:
            if self.check_speedy_rising_volumn(code):
                buy_list.append(code)

        self.update_buy_list(buy_list)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pymon = PyMon()
    pymon.run()
