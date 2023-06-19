import requests
from bs4 import BeautifulSoup

URL = 'https://www.musinsa.com/ranking/brand'

request = requests.get(URL)
html = request.text
soup = BeautifulSoup(html, 'html.parser')

brand_names = soup.select('p.brand_name')
brand_name_ens = soup.select('p.brand_name_en')

for i in range(len(brand_names)):
    brand_name = brand_names[i].text.strip().split('\n')[0]
    brand_name_en = brand_name_ens[i].text.strip().split('\n')[0]
    print('{:3}위. {}({})'.format(i + 1, brand_name, brand_name_en))

# 검색 기능
search_query = input("브랜드를 검색하면 순위를 알 수 있습니다: ")

found = False
for i in range(len(brand_names)):
    brand_name = brand_names[i].text.strip().split('\n')[0]
    brand_name_en = brand_name_ens[i].text.strip().split('\n')[0]
    
    if search_query in brand_name or search_query in brand_name_en:
        found = True
        print('해당 브랜드는 {}위입니다:\n{}({})'.format(i + 1, brand_name, brand_name_en))

if not found:
    print('브랜드를 찾을 수 없습니다.')
