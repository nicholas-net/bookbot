def get_books_text(path_to_file) -> str:
    """
    Opens the book file and returns the contents of the book as a str.

    Args:
            path_to_file : relative directory location of the file.

    Returns:
        str: the text of the frankenstein book.
    """

    with open(path_to_file) as frankenstein_file:
        # Returns all the bytes of the file as a string.
        file_contents = frankenstein_file.read()
    return file_contents

def get_number_of_words(book_text: str) -> int:
    """
    Splits each word from the file into an array. Total counter represents the number of words
    in the book. Increments every loop.

    Args:
        book_text (str) : books text.

    Returns
        int: total word count.

    """
    words = book_text.split()
    return len(words)

def get_character_frequency(book_text: str) -> dict:
    """
    Count the total frequency of characters from the book. Returns characters and frequencies as
    a key, value pair.

    Args:
        book_text (str) : text file content.

    Returns:
        dict: dictionary with every characters frequency returned.
    """

    #New dictionary to store the frequencies.
    frequency = {}
    #Eliminates capitalization's.
    book_text = book_text.lower()
    #Create a set of each unique character found to use the count function on each one.
    for letter in set(book_text):
        frequency[letter] = book_text.count(letter)

    return frequency

def sort_on(char_frequencies):
    """
    Lets the sort function know what key to sort the dictionaries on.

    Args:
        char_frequencies (dict) : dictionary of character frequencies from the book.
    """
    return char_frequencies["num"]

def sort_frequency(character_frequencies: dict) -> list:
    """
    Sort the character count in descending order.

    Args:
        character_frequencies (dict) : dictionary of characters and frequency.

    Returns:
        list: sorted list of dictionaries.
    """

    #Holds the character dictionaries in a list.
    sorted_dictionaries = []

    #Loops through each character key and total value.
    for char, count in character_frequencies.items():
        #Initializes a new seperate dictionary to hold each char and count pair.
        sorted_dictionaries.append({"char": char, "num": count})
        # Sorts the list by largest count, in ascending order.
    sorted_dictionaries.sort(reverse=True,key=sort_on)
    return sorted_dictionaries


def _analyze_book_path(book_path) -> str:
    """
    Helper function provides modularity and encapsulates the logic.

    Args:
        book_path (str) : book location in directory.

    Returns:
        str: text printing what book and directory is being analyzed, otherwise
        prints it cannot be found.
    """
    import os
    if not os.path.exists(book_path):
        return f"Error: no book found at {book_path}"
    return f"Analyzing book found at {book_path}..."


def print_interface(book_path: str, total_word_count, char_frequencies) -> None:
    """
    Prints book path, total words and total letters for the user to read in a clean console interface

    Args:
        (str) book_path :
        (int) total_word_count :
        (int) char_frequencies :

    Returns:
        organized console interface printing the path, word count, and character count.
    """

    print("============ BOOKBOT ============")
    print(_analyze_book_path(book_path))
    print("----------- Word Count ----------")
    print(f"Found {total_word_count} total words")
    print("--------- Character Count -------")

    for dictionary in char_frequencies:
        # Only prints alphabetical letters.
        if not dictionary["char"].isalpha():
            continue

        print(f"{dictionary["char"]}: {dictionary["num"]}")

    print("============= END ===============")















