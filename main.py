#All code written by Nicholas Colon

from stats import get_number_of_words, get_books_text, get_character_frequency, sort_frequency, print_interface


def main():
    book_path = "books/frankenstein.txt"
    text = get_books_text(book_path)
    num_words = get_number_of_words(text)
    dict = get_character_frequency(text)
    sorted_char_count = sort_frequency(dict)
    print_interface(book_path, num_words, sorted_char_count)

main()

