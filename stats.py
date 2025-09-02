def words_count(words):
    separated_words = words.split()
    return len(separated_words)

def repeat_count(words):
    words_lowercase = words.lower()
    word_dictionary = {}

    for char in words_lowercase:
        word_dictionary[char] = word_dictionary.get(char,0) + 1

    return word_dictionary

def sort_on(d):
    return d["num"]

def sort_dictionary_to_list(dictionary_words):
    #dict(sorted(dictionary_words.items(), key=lambda item: item[1], reverse= True))
    sorted_list = []
    for key in dictionary_words:
        sorted_list.append({"char": key, "num": dictionary_words[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list