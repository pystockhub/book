import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime

def get_financial_statements(code):
    url = "http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd=%s&fin_typ=0&freq_typ=Y" % (code)
    html = requests.get(url).text

    html = html.replace('<th class="bg r01c02 endLine line-bottom"colspan="8">연간</th>', "")
    html = html.replace("<span class='span-sub'>(IFRS연결)</span>", "")
    html = html.replace("<span class='span-sub'>(IFRS별도)</span>", "")
    html = html.replace('\t', '')
    html = html.replace('\n', '')
    html = html.replace('\r', '')

    html = html.replace('2011/12', '2011')
    html = html.replace('2012/03', '2011')
    html = html.replace('2012/12', '2012')
    html = html.replace('2013/03', '2012')
    html = html.replace('2013/12', '2013')
    html = html.replace('2014/03', '2013')
    html = html.replace('2014/12', '2014')
    html = html.replace('2015/03', '2014')
    html = html.replace('2015/12', '2015')

    df_list = pd.read_html(html, index_col='주요재무정보')
    df = df_list[0]
    return df

def get_3year_treasury():
    url = "http://www.index.go.kr/strata/jsp/showStblGams3.jsp?stts_cd=107301&idx_cd=1073"
    html = requests.get(url).text

    soup = BeautifulSoup(html, 'lxml')
    tr_data = soup.find_all('tr', id='tr_107301_1')
    td_data = tr_data[0].find_all('td')

    treasury_3year = {}
    start_year = 1997

    for x in td_data:
        treasury_3year[start_year] = x.text
        start_year += 1

    return treasury_3year

def get_dividend_yield(code):
    url = "http://companyinfo.stock.naver.com/company/c1010001.aspx?cmp_cd=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, 'lxml')
    td_data = soup.find_all('td', {'class': 'cmp-table-cell td0301'})
    dt_data = td_data[0].find_all('dt')

    dividend_yield = dt_data[5].text
    dividend_yield = dividend_yield.split(' ')[1]
    dividend_yield = dividend_yield[:-1]
    return dividend_yield

def get_estimated_dividend_yield(code):
    df = get_financial_statements(code)

    column = df.columns[5]
    cur_year = df[column]
    estimated_dividend_yield = cur_year['현금배당수익률']
    return estimated_dividend_yield

def get_previous_dividend_yield(code):
    df = get_financial_statements(code)
    dividend_yields = df.ix['현금배당수익률']

    ret = {}
    now = datetime.datetime.now()
    year = now.year - 5

    for dividend_yield in dividend_yields.values:
        ret[year] = dividend_yield
        year += 1

    return ret

def get_current_3year_treasury():
    url = "http://info.finance.naver.com/marketindex/interestDailyQuote.nhn?marketindexCd=IRR_GOVT03Y&page=1"
    html = requests.get(url).text

    soup = BeautifulSoup(html, 'lxml')
    tbody_data = soup.find_all('tbody')
    tr_data = tbody_data[0].find_all('tr')
    td_data = tr_data[0].find_all('td')
    return td_data[1].text

if __name__ == "__main__":
    #print(get_dividend_yield('058470'))
    #print(get_estimated_dividend_yield('058470'))
    #print(get_current_3year_treasury())
    print(get_previous_dividend_yield('058470'))


