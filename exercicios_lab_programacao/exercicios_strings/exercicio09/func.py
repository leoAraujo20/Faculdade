def sei_la(words_list, other_words):
    new_list = [word if word in other_words else word[0] for word in words_list]
    return new_list


