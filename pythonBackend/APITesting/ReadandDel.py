import json
import requests
from APITesting.payload import *
from utilties.configuration import *

################  ADDITION OF THE BOOK ########################################

response = requests.post(getconfig()['API']['endpoint'] + '/Library/Addbook.php', json=addpayload("abcd"),
                         headers={"Content-type": "application/json"}, )
book_response = response.json()
print(book_response["ID"])
BookID = book_response["ID"]

################  DELETION OF THE BOOK ########################################

del_response = requests.post("https://rahulshettyacademy.com/Library/DeleteBook.php", json={
    "ID": BookID}, headers={"Content-type": "application/json"})
assert del_response.status_code == 200
output = del_response.json()
print(output['msg'])
assert output['msg'] == "book is successfully deleted"
