import sys

from stats import get_num_words, high_to_low_character_counts, letter_count


def get_book_text(filepath: str):
    """
    Args:
        filepath: path to source file

    Returns:
        A String containing the contents of the input file

    Raises:
        None
    """

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text.split())
    character_dictionary = letter_count(book_text)
    sorted_char_list = high_to_low_character_counts(character_dictionary)
    print(f"""
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for element in sorted_char_list:
        character = element["char"]
        if character.isalpha():
            print(f"{character}: {element['num']}")
    print("============= END ===============")


main()
