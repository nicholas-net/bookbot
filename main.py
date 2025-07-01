#All code written by Nicholas Colon
from stats import get_number_of_words, get_books_text

def main():
    book = "books/frankenstein.txt"
    text = get_books_text(book)
    get_number_of_words(text)

main()

