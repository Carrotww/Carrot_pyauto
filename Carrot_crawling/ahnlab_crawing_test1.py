from bs4 import BeautifulSoup
import requests

myheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.114 Whale/3.17.145.12 Safari/537.36'}
url = "https://ahnlab.recruiter.co.kr/app/jobnotice/list"
url2 = "https://career.programmers.co.kr/job?page=10&min_career=0&order=recent"

response = requests.get(url, headers=myheader)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    title = soup.select_one('#divJobnoticeList > ul > li:nth-child(1) > div:nth-child(2) > h2 > span > a')
    title2 = soup.select('#list-positions-wrapper > ul > li:nth-child(1) > div.item-body > ul.list-position-tags')
    for ti in title2:
        print(ti)
    print(title2)
else:
    print(response.status_code)