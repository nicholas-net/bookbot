#All code written by Nicholas Colon

import sys
from stats import get_number_of_words, get_books_text, get_character_frequency, sort_frequency, print_interface


def main():

    # Expect one argument: the relative path to the book (argv[0] is script name).
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
    else:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_books_text(book_path)
    num_words = get_number_of_words(text)
    character_dict = get_character_frequency(text)
    sorted_char_count = sort_frequency(character_dict)
    print_interface(book_path, num_words, sorted_char_count)

if __name__ == '__main__':
    main()

