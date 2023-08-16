#!/usr/bin/python3
def read_file(filename=""):
    """This functuion read files and prints to stdout

    Args:
        filename (string): name of the file
    """

    with open(filename, 'r') as file:
        file_data = file.read()
        file.close()
    print(file_data)
