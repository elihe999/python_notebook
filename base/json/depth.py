# -*- coding: utf-8 -*-
"""
@file: json

"""

import json

def get_list_depth(input_list, input_depth):
    """
    @funtion: loop
    """
    max_number = input_depth
    for item in input_list:
        if type(item).__name__ == "dict":
            current_level = input_depth
            for KEY, VALUE in item.items():
                if type(VALUE).__name__ == "list":
                    if VALUE != [] and KEY != "optionList":
                        temp_compare_num = get_list_depth(VALUE, current_level+1)
                        if temp_compare_num > max_number:
                            max_number = temp_compare_num
                            print(max_number)
    return max_number


if __name__ == "__main__":
    ROOT_CHILDREN = open('./test2.json').read()
    DATA_LIST = json.loads(ROOT_CHILDREN)
    MAINDEPTH = 1
    if type(DATA_LIST).__name__ == 'list':
        NUMBER_DEPTH = get_list_depth(DATA_LIST, MAINDEPTH)
        print("@@finial@@:", NUMBER_DEPTH)
    else:
        print(type(DATA_LIST))

