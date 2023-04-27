#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """This function divides element in list \
        by another element in list of the same position

    Args:
        my_list_1 (list): first list
        my_list_2 (list): second list

    Returns:
        list of result
    """

    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            continue

    return new_list