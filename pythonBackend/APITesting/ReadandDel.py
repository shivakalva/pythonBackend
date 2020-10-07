import json
import requests
from APITesting.payload import *
from utilties.configuration import *
from utilties.resources import *

################  ADDITION OF THE BOOK ########################################

url = getconfig()['API']['endpoint'] + ApiResources.addBook
headers = {"Content-type": "application/json"}
response = requests.post(url, json=addpayload("abcd"), headers=headers, )
book_response = response.json()
print(book_response["ID"])
BookID = book_response["ID"]

################  DELETION OF THE BOOK ########################################

durl = getconfig()['API']['endpoint'] + ApiResources.deleteBook
del_response = requests.post(durl, json={
    "ID": BookID}, headers=headers, )
assert del_response.status_code == 200
output = del_response.json()
print(output['msg'])
assert output['msg'] == "book is successfully deleted"
