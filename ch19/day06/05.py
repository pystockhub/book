import requests

response = requests.get("https://companyinfo.stock.naver.com/v1/company/c1010001.aspx?cmp_cd=035720")
print(response.text)


