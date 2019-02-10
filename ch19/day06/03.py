from bs4 import BeautifulSoup

html = '''
<ul>
	<li> 100 </li>
	<li> 200 </li>
</ul>
<ol>
	<li> 300 </li>
	<li> 400 </li>
</ol>
'''
soup = BeautifulSoup(html, 'html5lib')    
result = soup.select('ul li')
print(result)