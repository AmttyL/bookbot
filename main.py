from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    char_count = text_from_book(text)
    new_list = sorted_dictionary(char_count)
    final_print(num_words, file_path, new_list)



def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

main()


