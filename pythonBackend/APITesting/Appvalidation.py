import requests
import json
from APITesting.payload import *
from utilties.configuration import *
from utilties.resources import *


URL = getconfig()['API']['endpoint']+ ApiResources.addBook
headers = {"Content-type": "application/json"}
query = "select * from customerinfo"
addBook_response = requests.post(URL, json=getpayloadFromdb("query"), headers=headers, )

response_json = addBook_response.json()
print(type(response_json))

for book in response_json:
    if response_json['ID'] == 'hli124':
        print(book)
        break

expectedbook = {
    "name": "Learn Appium Automation with Java",
    "isbn": "hhjj",
    "aisle": "2017",
    "author": "John foe"
}
assert book == expectedbook
