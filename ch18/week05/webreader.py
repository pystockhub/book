import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_financial_statements(code):
    url = "http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd=%s&fin_typ=0&freq_typ=Y" % (code)
    html = requests.get(url).text

    html = html.replace('<th class="bg r01c02 endLine line-bottom"colspan="8">연간</th>', "")
    html = html.replace("<span class='span-sub'>(IFRS연결)</span>", "")
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
    tr_data = soup.findAll('tr', id='tr_107301_1')
    td_data = tr_data[0].find_all('td')

    treasury_3year = {}
    start_year = 1997

    for x in td_data:
        treasury_3year[start_year] = x.text
        start_year += 1

    print(treasury_3year)
    return treasury_3year

if __name__ == "__main__":
    #get_financial_statements('035720')
    get_3year_treasury()


