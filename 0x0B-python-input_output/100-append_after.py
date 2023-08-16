#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """This function inserts a line after a particular line

    Args:
        filename (string): name of file
        search_string (string): text line to find
        new_string (string): new string to insert
    """

    text_lines = []
    with open(filename, 'r') as file:
        for line in file:
            text_lines.append(line.strip())

    with open(filename, 'a') as file:
        for line in text_lines:
            words = line.split()
            for word in words:
                #print(word)
                if search_string in word:
                    file.write(new_string)
                    break
