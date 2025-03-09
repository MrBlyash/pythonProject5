from bs4 import BeautifulSoup
import requests

response = requests.get("https://sinoptik.ua/ru/pohoda/nikopol")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
soup_list = soup.find_all(class_="RSWdP9mW X6TmI5bI")
res = soup_list[0]
print(res.text)

response = requests.get("https://sinoptik.ua/ru/pohoda/nikopol")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
soup_list = soup.find_all(class_="yQxWb1P4")
res = soup_list[0]
print(res.text)

response = requests.get("https://sinoptik.ua/ru/pohoda/nikopol")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
soup_list = soup.find_all(class_="R1ENpvZz")
res = soup_list[0]
print(res.text)
