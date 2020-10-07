import requests
from utilties.configuration import *

url = "https://api.github.com/user"
github_response = requests.get(url, verify= False, auth=('shivakalva',getpwd()))
print(github_response.status_code)