from datetime import datetime
import requests
from bs4 import BeautifulSoup
import fake_useragent
from multiprocessing import Process

user = fake_useragent.UserAgent().random
header = {'user-agent': user, }
page = 1
max_page = 10
list_words = []

start_time = datetime.now()
while page < max_page:
    link = f'https://bezbukv.ru/mask/*****?page={page}'
    responce = requests.get(link, headers=header).text
    soup = BeautifulSoup(responce, 'lxml')
    block = soup.find('div', id="yw1")
    list_view = block.find_all('div', class_='view')
    for view in list_view:
        print(f'{view.text[-7:-2]}')
        list_words.append(view.text[-7:-2])
    page += 1

result = []
black_list_letter = ['г', 'л', 'с', 'п', 'р', 'б', 'и', 'к', 'т']
black_list_word = []
for word in list_words:
    for letter in word:
        if letter in black_list_letter:
            black_list_word.append(word)
# убираем повторы
black_list_word = list(set(black_list_word))

for word in list_words:
    if word in black_list_word:
        continue
    result.append(word)
print(result)
print(datetime.now() - start_time)
