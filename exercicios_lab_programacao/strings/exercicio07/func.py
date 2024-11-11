def first_letter(words_list):
    first_letters = []
    for word in words_list:
        first_letters.append(word[0])
    return '. '.join(first_letters)