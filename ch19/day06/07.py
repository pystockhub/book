import requests
import re
from bs4 import BeautifulSoup


code = "035720"
re_enc = re.compile("encparam: '(.*)'", re.IGNORECASE)
re_id = re.compile("id: '([a-zA-Z0-9]*)' ?", re.IGNORECASE)

url = "https://companyinfo.stock.naver.com/v1/company/c1010001.aspx?cmp_cd={}".format(code)
html = requests.get(url).text
encparam = re_enc.search(html).group(1)
encid = re_id.search(html).group(1)

url = "https://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd={}&fin_typ=0&freq_typ=A&encparam={}&id={}".format(
    code, encparam, encid)
headers = {"Referer": "HACK"}
html = requests.get(url, headers=headers).text

soup = BeautifulSoup(html, "html5lib")
dividend = soup.select("table:nth-of-type(2) tr:nth-of-type(33) td span")
years = soup.select("table:nth-of-type(2) th")

print(years)
print(dividend)