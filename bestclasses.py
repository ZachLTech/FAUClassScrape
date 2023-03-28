import requests
from bs4 import BeautifulSoup

url = "https://www.fau.edu/registrar/courses/ClassroomSchedule.php"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

cells = soup.select("td")
text = soup.get_text()


with open('data.txt', 'w') as data:
    data.write(text)
