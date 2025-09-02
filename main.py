import sys
from stats import words_count, repeat_count, sort_dictionary_to_list

def get_book_text(file_path):
    contents = None
    with open(file_path) as f:
        contents = f.read()

    return contents

def beautify_dic(sort_list):
    # dictionary is sorted, we just need to print line at a time
    for item in sort_list:
        if (item["char"].isalpha()):
            print(f"{item['char']}: {item['num']}")

def print_log(book_path, count_total, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_total} total words")
    print("--------- Character Count -------")
    beautify_dic(sorted_list)
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    count_total = words_count(get_book_text(book_path))
    sorted_list = sort_dictionary_to_list(repeat_count(get_book_text(book_path)))

    print_log(book_path, count_total, sorted_list)


main()