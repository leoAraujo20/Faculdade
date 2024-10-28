from func import *

valid_words = ['da', 'de', 'das', 'do', 'dos', 'e']

word = input('Type one word:').lower()

print(is_valid_word(word, valid_words))