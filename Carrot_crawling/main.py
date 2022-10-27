from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

url = "https://ahnlab.recruiter.co.kr/app/jobnotice/list"
url2 = "https://career.programmers.co.kr/job?page=10&min_career=0&order=recent"

response = requests.get(url2)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#divJobnoticeList > ul > li:nth-child(1) > div:nth-child(2) > h2 > span > a')
    title2 = soup.select('#list-positions-wrapper > ul > li:nth-child(1) > div.item-body > ul.list-position-tags')
    for ti in title2:
        print(ti)
    print(title2)
else:
    print(response.status_code)