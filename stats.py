
def get_books_text(path_to_file) -> str:
    """
     Opens the frankenstein book file and returns the contents of the book as a str.

     Args:
            path_to_file : relative directory location of the frankenstein file.

    Returns:
        str: the text of the frankenstein book.
    """

    with open(path_to_file) as frankenstein_file:
        file_contents = frankenstein_file.read()
    return file_contents

def get_number_of_words(book_text):
    """
    Splits each word from the frankenstein file into an array. Total counter represents the number of words
    in the book. Increments every loop.

    Args:
        (str) : extracted frankenstein file text

    Returns
        int: total word count

    """
    words = book_text.split()
    total=0
    for word in words:
        total+=1
    print(f"{total} words found in the document")
