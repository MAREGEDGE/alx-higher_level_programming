#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    listlen = len(my_list) - 1

    if idx > listlen:
        return my_list

    elif idx < 0:
        return my_list

    else:
        my_list[idx] = element
        return my_list
