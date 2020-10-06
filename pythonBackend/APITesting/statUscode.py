import requests

response = requests.get("https://api.domainsdb.info/v1/domains/search",
                        params={'domain': 'facebook'}, )
status = response.status_code
headers = response.headers
# print(status)
# print(headers)
assert status == 200
assert response.headers['Content-Type'] == "application/json"
for check in response:
    if check['Connection'] == "keep - alive":
        print(check)
