import requests
from bs4 import BeautifulSoup
import fake_useragent
from threading import Thread
from datetime import datetime

user = fake_useragent.UserAgent().random
header = {'user-agent': user, }
start_time = datetime.now()


def parser(page, list_words):
    link = f'https://bezbukv.ru/mask/*****?page={page}'
    response = requests.get(link, headers=header).text
    soup = BeautifulSoup(response, 'lxml')
    block = soup.find('div', id="yw1")
    list_views = block.find_all('div', class_='view')
    for view in list_views:
        list_words.append(view.text[-7:-2])


def start_tread(list_words, max_pages=1):
    treads_list = []
    for i in range(1, max_pages + 1):
        thr = Thread(target=parser, args=(i, list_words,))
        treads_list.append(thr)
        print(f'Запушен процес {i}/{max_pages}')
    for thr in treads_list:
        thr.start()
        thr.join()


def get_black_list_words(list_words, black_list_letter):
    result_list_words = []
    for word in list_words:
        for letter in word:
            if letter in black_list_letter:
                result_list_words.append(word)
    result_list_words = list(set(result_list_words))
    return result_list_words


def get_word_needs_letter(list_words, list_needs_letters):
    blackList = []
    for letter in list_needs_letters:
        for word in list_words:
            if letter not in word:
                blackList.append(word)
    resault = [word for word in list_words if word not in blackList]
    return resault


def main():

    black_list_letters = ['а', 'р', 'б', ]
    # 'т', 'к', 'м', 'и', 'е',
    list_needs_letters = ['з', 'о', ]
    max_page = 42
    list_words = []

    start_tread(list_words, max_page)
    list_words = list(set(list_words))
    print(f'{len(list_words)} слов получил с сайта - {list_words}')

    black_words = get_black_list_words(list_words, black_list_letters)
    black_words = list(set(black_words))
    print(f'{len(black_words)} не подходят  - {black_words}')

    regular_list = []
    for word in list_words:
        if word not in black_words:
            regular_list.append(word)

    list_ = get_word_needs_letter(regular_list, list_needs_letters)
    list_.sort()
    print(f'{len(list_)} подходящие слова - {list_}')


if __name__ == '__main__':
    main()
