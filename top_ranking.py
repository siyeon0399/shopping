import requests
from bs4 import BeautifulSoup

# 상의 아이템 판매순 랭킹

URL = 'https://www.musinsa.com/categories/item/001?d_cat_cd=001&brand=&list_kind=small&sort=sale_high&sub_sort=1w&page=1&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='

request = requests.get(URL)
html = request.text
soup = BeautifulSoup(html, 'html.parser')

item_titles = soup.select('p.item_title')
list_infos = soup.select('p.list_info')
prices = soup.select('p.price')
points = soup.select('p.point')

for i in range(50):
    item_title = item_titles[i].text.strip().split('\n')[0]
    list_info = list_infos[i].text.strip().split('\n')[0]
    price = prices[i].text.strip().split('\n')[0]
    point = points[i].text.strip().split('\n')[0] if i < len(points) else '0'
    print('{:3}위. {}의 {} {} 리뷰 {}개)'.format(i + 1, item_title, list_info, price, point))

search_term = input('순위권 내 검색하고 싶은 브랜드를 입력하세요: ')

count = 0
for i in range(50):
    item_title = item_titles[i].text.strip().split('\n')[0]
    list_info = list_infos[i].text.strip().split('\n')[0]
    price = prices[i].text.strip().split('\n')[0]
    point = points[i].text.strip().split('\n')[0] if i < len(points) else '0'
    
    if search_term.lower() in item_title.lower():
        count += 1
        print('{}의 {} {} 리뷰 {}개)'.format(item_title, list_info, price, point))

if count == 0:
    print('검색 결과가 없습니다.')