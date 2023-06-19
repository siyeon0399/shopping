import subprocess

# 번호 입력하기
print('패션 사이트 무신사의 랭킹입니다.')
print('브랜드 랭킹과 상의 랭킹을 검색할 수 있습니다')
print('1. 브랜드 랭킹 2. 상의 랭킹')
user_input = input("검색하고 싶은 것의 숫자만 입력하세요: ")

if user_input == '1':
    subprocess.run(['python', 'brand_ranking.py'])
elif user_input == '2':
    subprocess.run(['python', 'top_ranking.py'])
else:
    print("잘못된 입력입니다.")