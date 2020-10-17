import requests
from bs4 import BeautifulSoup

li = []
result = requests.get("https://www.imdb.com/find?s=ep&q=thriller&ref_=nv_sr_sm")
content = BeautifulSoup(result.content, 'html.parser')
moviestable = content.find('table',{'class':'findList'})
rows = moviestable.findAll('tr')
for row in rows:
    rowdata = row.findAll('td')
    # print(rowdata[1].a.text)
    suburl = rowdata[1].a['href']
    subdata = requests.get("https://www.imdb.com/" + suburl)
    childsoup = BeautifulSoup(subdata.content, 'html.parser')
    if childsoup.find('div',{'class':'see-more inline canwrap'}):
        genre = childsoup.find('div',{'class':'see-more inline canwrap'})
        if genre.a.text == " Documentary":
            # print(rowdata[1].a.text)
            li.append(rowdata[1].a.text)
print(li)