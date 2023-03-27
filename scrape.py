import requests
url = input("Session URL: ")

cookie1 = input("_fpb= ")
cookie2 = input("_ga= ")
cookie3 = input("_gcl_au= ")
cookie4 = input("_hp2_id.= ")
cookie5 = input("BIGipServerboc22banxe_faup_StuRegSsb_pool= ")
cookie6 = input("fs_uid= ")
cookie7 = input("JSESSIONID= ")

cookies = dict(_fbp=cookie1, _ga=cookie2,_gcl_au=cookie3, _hp2_id=cookie4, BIGipServerboc22banxe_faup_StuRegSsb_pool=cookie5, fs_uid=cookie6, JSESSIONID=cookie7)
response = requests.get(url)


cookies_jar = requests.cookies.RequestsCookieJar()
cookies_jar.set('_fpb', cookie1, domain='bannerxe.fau.edu', path='/cookies')
cookies_jar.set('_ga', cookie2, domain='bannerxe.fau.edu', path='/cookies')
cookies_jar.set('_gcl_au', cookie3, domain='bannerxe.fau.edu', path='/cookies')
cookies_jar.set('_hp2_id.3001039959', cookie4, domain='bannerxe.fau.edu', path='/cookies')
cookies_jar.set('BIGipServerboc22banxe_faup_StuRegSsb_pool', cookie5, domain='bannerxe.fau.edu', path='/cookies')
cookies_jar.set('fs_uid', cookie6, domain='bannerxe.fau.edu', path='/cookies')
cookies_jar.set('JSESSIONID', cookie7, domain='bannerxe.fau.edu', path='/cookies')
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.find_all)

#https://bannerxe.fau.edu/StudentRegistrationSsb/ssb/courseSearchResults/courseSearchResults?txt_term=202308&startDatepicker=&endDatepicker=&uniqueSessionId=00ei41679808151588&pageOffset=0&pageMaxSize=10&sortColumn=subjectDescription&sortDirection=asc