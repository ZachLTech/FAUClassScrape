import requests
from bs4 import BeautifulSoup

url = "https://www.fau.edu/registrar/courses/ClassroomSchedule.php"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

cells = soup.select("td")
text = soup.get_text()
print(text)