import requests

#Sending the file as an attachment

URL = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('C:\\MySpace\\PythonPRAC\\food.jpg', 'rb')}
resp = requests.post(URL, files=files)
print(resp.status_code)
print(resp.text)
