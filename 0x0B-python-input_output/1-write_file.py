#!/usr/bin/python3
def write_file(filename="", text=""):
    """This function write to a file

    Args:
        filename (string): name of the file to write to
        text (string): Words to write

    Returns:
        Number of characters written
    """

    with open(filename, 'w') as file:
        nb_of_chars = file.write(text)  # Number of characters written
        file.close()
    return nb_of_chars
