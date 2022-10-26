from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

url = "https://ahnlab.recruiter.co.kr/app/jobnotice/list"

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#divJobnoticeList > ul > li:nth-child(1) > div:nth-child(2) > h2 > span > a')
    print(title)
else:
    print(response.status_code)