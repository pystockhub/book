import requests
import pandas as pd

def get_financial_statements(code):
    url = "http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd=%s&fin_typ=0&freq_typ=Y" % (code)
    html = requests.get(url).text

    df_list = pd.read_html(html, index_col="주요재무정보")
    df = df_list[0]
    print(df)

if __name__ == "__main__":
    get_financial_statements('035720')
