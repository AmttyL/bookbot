def get_num_words(text):
    words_split = text.split()
    return len(words_split)

def text_from_book(text):
    char_count = {}
    for char in text.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sorted_dictionary(dict_name):
    new_list = []
    for key in dict_name:
        new_dict = {
            "char": key,
            "num": dict_name[key]
        }
        new_list.append(new_dict)
    new_list.sort(reverse=True, key=sort_on)

    return new_list

def sort_on(num):
    return num["num"]

def final_print(words, path, list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for l in list:
        if l["char"].isalpha():
            print(f"{l["char"]}: {l["num"]}")
    print("============= END ===============")
