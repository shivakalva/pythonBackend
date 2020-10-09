import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.imdb.com/find?q=thriller&ref_=nv_sr_sm")
soup = BeautifulSoup(data.content, 'html.parser')
#print(soup.prettify())
moviestable = soup.find('table', {'class':'findList'})
#print(moviestable)
#moviestable.findAll('tr')
rows = moviestable.findAll('tr')
for row in rows:
    rowdata = row.findAll('td')
    print(rowdata[1].a.text)
    suburl = rowdata[1].a['href']
    print(suburl)