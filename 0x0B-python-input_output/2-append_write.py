#!/usr/bin/python3
def append_write(filename="", text=""):
    """This function add text to a file

    Args:
        filename (string): name of the file
        text (string): text to add

    Returns:
        Number of characters added
    """

    with open(filename, 'a') as file:
        nb_of_chars_added = file.write(text)
        file.close()

    return nb_of_chars_added
