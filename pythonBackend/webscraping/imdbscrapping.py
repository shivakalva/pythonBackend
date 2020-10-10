import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.imdb.com/find?s=ep&q=thriller&ref_=nv_sr_sm")
content = BeautifulSoup(result.content, 'html.parser')
moviestable = content.find('table',{'class':'findList'})
rows = moviestable.findAll('tr')
for row in rows:
    rowdata = row.findAll('td')
    print(rowdata[1].a.text)
