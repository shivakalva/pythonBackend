import requests

# https://rahulshettyacademy.com/
# visit-month is cookie in above site

Cookie = {'visit-month': 'February'}
response = requests.get('https://rahulshettyacademy.com/',cookies=Cookie)
print(response.status_code)


### this will sent the cookies back and we can give addl. to the session

se = requests.session()
se.cookies.update({'visit-month': 'February'})  # this will preload the cookie since we are updating
response = se.get("https://httpbin.org/cookies", cookies={'visit-year': '2020'})
print(response.text)



