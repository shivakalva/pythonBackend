import json
import requests
# from payload import *
import configparser


################ USE THE METHOD FOR STORING THE PAYLOAD DATA ########################################

def addpayload(isbn):
    body = {

        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": "124",
        "author": "John foe"
    }
    return body


################  ADDITION OF THE BOOK ########################################
config = configparser.ConfigParser()
config.read('utilities/properties.ini')
response = requests.post(config['API']['endpoint'] + '/Library/Addbook.php', json=addpayload("hjkl"),
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
