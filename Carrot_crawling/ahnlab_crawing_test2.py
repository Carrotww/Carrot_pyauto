from bs4 import BeautifulSoup
import requests

url = "https://ahnlab.recruiter.co.kr/app/jobnotice/list"
myheader = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.114 Whale/3.17.145.12 Safari/537.36'}

response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

temp = soup.find_all('span', {'class': 'list-bbs-notice-name'})

print(temp)