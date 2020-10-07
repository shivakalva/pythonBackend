import requests

# https://rahulshettyacademy.com/
# visit-month is cookie in above site
# allow_redirects=False stops after giving first showing status code

Cookie = {'visit-month': 'February'}
response = requests.get('http://rahulshettyacademy.com/',allow_redirects=False, cookies=Cookie)
print(response.history)  # gives the status code 301 and 200
print(response.status_code)

#########################################################################################
### Below API will sent the cookies back so that we can verify what has come back and we can give addl. properties to the session

se = requests.session()
cooki={'visit-year': '2020'}
se.cookies.update({'visit-month': 'February'})  # this will preload the cookie since we are updating
response = se.get("https://httpbin.org/cookies", allow_redirects=False, cookies=cooki, timeout=1)
print(response.status_code)

#301 #200 -- First it will hit another Api and retuns 301 and then actual above one and it gives 200, to disable it use
#allow_redirection flaf to false

print(response.text)



