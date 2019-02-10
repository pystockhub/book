import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import datetime
pd.set_option('display.expand_frame_repr', False)

import re



def get_financial_statements(code):   
    # 인증값 추출
    re_enc = re.compile("encparam: '(.*)'", re.IGNORECASE)
    re_id = re.compile("id: '([a-zA-Z0-9]*)' ?", re.IGNORECASE)
    
    url = "https://companyinfo.stock.naver.com/v1/company/c1010001.aspx?cmp_cd={}".format(code)
    html = requests.get(url).text
    
    search = re_enc.search(html)
    if search is None:
        return {}    
    encparam = re_enc.search(html).group(1)
    encid = re_id.search(html).group(1)
        
    # 스크래핑
    url = "https://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd={}&fin_typ=0&freq_typ=A&encparam={}&id={}".format(code, encparam, encid)
    headers = {"Referer": "HACK"}
    html = requests.get(url, headers=headers).text
    
    soup = BeautifulSoup(html, "html5lib")
    dividend = soup.select("table:nth-of-type(2) tr:nth-of-type(33) td span")                      
    years = soup.select("table:nth-of-type(2) th")                      
        
    dividend_dict = {}
    for i in range(len(dividend)):
        dividend_dict[years[i+3].text.strip()[:4]] = dividend[i].text
    
    return dividend_dict
    

def get_3year_treasury():
    url = "http://www.index.go.kr/strata/jsp/showStblGams3.jsp?stts_cd=288401&amp;idx_cd=2884&amp;freq=Y&amp;period=1998:2018"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')
    td_data = soup.select("tr td")
        
    treasury_3year = {}
    start_year = 1998

    for x in td_data:
        treasury_3year[start_year] = x.text
        start_year += 1

    return treasury_3year


def get_dividend_yield(code):
    url = "http://companyinfo.stock.naver.com/company/c1010001.aspx?cmp_cd=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, 'html5lib')
    dt_data = soup.select("td dl dt")
    
    dividend_yield = dt_data[-2].text
    dividend_yield = dividend_yield.split(' ')[1]
    dividend_yield = dividend_yield[:-1]

    return dividend_yield


def get_estimated_dividend_yield(code):
    dividend_yield = get_financial_statements(code)    
    if len(dividend_yield) == 0:
        return 0
    dividend_yield = sorted(dividend_yield.items())[-1]
    return dividend_yield[1]
            

def get_current_3year_treasury():
    url = "http://finance.naver.com/marketindex/interestDailyQuote.nhn?marketindexCd=IRR_GOVT03Y&page=1"
    html = requests.get(url).text

    soup = BeautifulSoup(html, 'html5lib')
    td_data = soup.select("tr td") 
    return td_data[1].text


def get_previous_dividend_yield(code):
    dividend_yield = get_financial_statements(code)    

    now = datetime.datetime.now()
    cur_year = now.year

    previous_dividend_yield = {}
    
    for year in range(cur_year-5, cur_year):
        if str(year) in dividend_yield:            
            previous_dividend_yield[year] = dividend_yield[str(year)]

    return previous_dividend_yield


if __name__ == "__main__":
    estimated_dividend_yield = get_estimated_dividend_yield("058470")
    print(estimated_dividend_yield)
    current_3year_treasury = get_current_3year_treasury() 
    print(current_3year_treasury)
    estimated_dividend_to_treasury = float(estimated_dividend_yield) / float(current_3year_treasury)
    print(estimated_dividend_to_treasury)
    # print(get_estimated_dividend_yield('058470'))
    # print(get_current_3year_treasury())
    # print(get_previous_dividend_yield('058470'))

