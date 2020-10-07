import json
import requests
from  utilties.configuration import *
from utilties.resources import *

# creating a session for Authentication and optimization of authentication
se = requests.session()
se.auth = auth =('shivakalva',getpwd())

urlrepos = "https://api.github.com/user/repos"
github_response = se.get(urlrepos)
print(github_response.status_code)

