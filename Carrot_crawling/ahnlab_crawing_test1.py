from bs4 import BeautifulSoup
import requests

# myheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.114 Whale/3.17.145.12 Safari/537.36'}
url = "https://ahnlab.recruiter.co.kr/app/jobnotice/list"
url2 = "https://career.programmers.co.kr/job?page=10&min_career=0&order=recent"

response = requests.get(url)
# response = requests.get(url, headers=myheader)
# 
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.find('div', {'class': 'list-bbs with-tab'})
    # thumbnail_url = soup.find('div', {'class': 'thumb'}).find('a').find('img')['src']

    print(title)
else:
    print(response.status_code)