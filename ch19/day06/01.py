from bs4 import BeautifulSoup

html = '''
<html>
<table border=1>
	<tr>
		<td> 항목 </td>
		<td> 2013 </td>
		<td> 2014 </td>
		<td> 2015 </td>
	</tr>

	<tr>
		<td> 매출액 </td>
		<td> 100 </td>
		<td> 200 </td>
		<td> 300 </td>
	</tr>
</table>
</html>
'''
soup = BeautifulSoup(html, 'html5lib')    
result = soup.select('td')
print(result)