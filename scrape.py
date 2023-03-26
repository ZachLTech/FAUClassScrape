import requests
url = input("Session URL: ")

cookie1 = input("BIGipServerboc22banxe_faup_StuRegSsb_pool= ")
cookie2 = input("JSESSIONID= ")

cookies = dict(BIGipServerboc22banxe_faup_StuRegSsb_pool=cookie1, JSESSIONID=cookie2)
response = requests.get(url)


cookies_jar = requests.cookies.RequestsCookieJar()
cookies_jar.set('BIGipServerboc22banxe_faup_StuRegSsb_pool', cookie1, domain='bannerxe.fau.edu', path='/')
cookies_jar.set('JSESSIONID', cookie2, domain='bannerxe.fau.edu', path='/StudentRegistrationSsb')
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.find_all)