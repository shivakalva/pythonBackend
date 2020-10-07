import requests

url = 'https://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}

reponse = requests.post(url, files=files)

###### Need to look into the below code ##########
# reponse.text
# {
#   ...
#   "files": {
#     "file": "<censored...binary...data>"
#   },
#   ...
# }