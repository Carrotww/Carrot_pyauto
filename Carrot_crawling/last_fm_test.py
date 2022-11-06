from bs4 import BeautifulSoup
import requests

# myheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.114 Whale/3.17.145.12 Safari/537.36'}
url = 'https://www.last.fm/music/%EB%B2%84%EC%A6%88/_/%EC%82%AC%EB%9E%91%EC%9D%80+%EA%B0%80%EC%8A%B4%EC%9D%B4+%EC%8B%9C%ED%82%A8%EB%8B%A4'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.find('div', {'class': "js-video-preview-playlink video-preview-playlink"})
    img = soup.find('img', {'class': "video-preview"})
    raw_data = soup.find('a', {'class': "image-overlay-playlink-link js-playlink"})['data-youtube-url']
    # thumbnail_url = soup.find('div', {'class': 'thumb'}).find('a').find('img')['src']

    # print(title)
    # print(img)
    print(raw_data)
else:
    print(response.status_code)