def get_num_words(list_of_words: list[str]) -> int:
    """
    Args:
        list_of_words: a list of words to count

    Returns:
        A count of words in the list

    Raises:
        None
    """
    return len(list_of_words)


def letter_count(text_to_analyze: str) -> dict[str, int]:
    """
    Args:
        text_to_analyze: text to count characters from

    Returns:
        A dictionary with counts of each character found

    Raises:
        None
    """
    character_count = {}
    lowercase_text = text_to_analyze.lower()
    for char in lowercase_text:
        if char in character_count:
            character_count[char] = character_count[char] + 1
            continue
        character_count[char] = 1
    return character_count


def getNum(list_element):
    return list_element["num"]


def high_to_low_character_counts(unsorted_dict: dict):
    """
    Args:
        unsorted_dict: dictionary of characters and their associated count

    Returns:
        A list of dictionaries containing a character and and its associated count using "char" and "num" as keys

    Raises:
        None
    """
    sorted_list = []
    for key in unsorted_dict.keys():
        temp_dictionary = {"char": key, "num": unsorted_dict[key]}
        sorted_list.append(temp_dictionary)

    sorted_list.sort(key=getNum, reverse=True)

    return sorted_list
