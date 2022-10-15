def get_word_needs_letter(list_words, list_needs_letters):
    blackList = []
    for letter in list_needs_letters:
        for word in list_words:
            if letter not in word:
                blackList.append(word)
    resault = [word for word in list_words if word not in blackList]
    return resault


a = ['123', '4569', '789', '11', '12', '13', '1954', ]
b = ['4', '5', '9']

print(get_word_needs_letter(a, b))
