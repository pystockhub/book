import requests

def get_financial_statements(code):
    url = "http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd=%s&fin_typ=0&freq_typ=Y" % (code)
    html = requests.get(url).text
    print(html)
    #print(type(requests.get(url)))
    #print(type(requests.get(url).text))

if __name__ == "__main__":
    get_financial_statements('035720')
