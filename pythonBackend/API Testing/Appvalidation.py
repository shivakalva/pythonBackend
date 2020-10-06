import requests
import json

addBook_response = requests.post("https://rahulshettyacademy.com/Library/Addbook.php", json={
    "name": "Learn Appium Automation with Java",
    "isbn": "hli",
    "aisle": "124",
    "author": "John foe"
}, headers={"Content-type": "application/json"}, )

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
