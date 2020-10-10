import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia")
soup = BeautifulSoup(data.content, 'html.parser')
results = soup.find(id='SearchResults',class_='mux-card mux-job-card')
title_elem = results.find('h2', class_='title')
company_elem = results.find('div', class_='company')
location_elem = results.find('div', class_='location')
print(title_elem.text.strip())
print(company_elem.text.strip())
print(location_elem.text.strip())
print()
#title_elem = job_elem.find_all('span', class_='name')

#print(results)
#rint(results.prettify())
# moviestable = soup.find('table', {'class':'findList'})
# #print(moviestable)
# #moviestable.findAll('tr')
# rows = moviestable.findAll('tr')
# for row in rows:
#     rowdata = row.findAll('td')
#     print(rowdata[1].a.text)
#     suburl = rowdata[1].a['href']
#     print(suburl)