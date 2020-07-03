def str2arr(str):
    return [i for i in str]


def arr2str(arr, join_parameter = ""):
    arr = [str(i) for i in arr]
    return join_parameter.join(arr)





def delete_spaces(arr):
    return [i for i in arr if i != " "]


def connect_numbers(arr):
    numbers, cur_num = "0123456789", ""
    res = []

    for i, elem in enumerate(arr):
        if elem in numbers:
            cur_num += elem
        else:
            if len(cur_num) > 0:
                res.append(cur_num)
                cur_num = ""
            res.append(elem)

    if len(cur_num) > 0: res.append(cur_num)

    return res


def find_last_symbol(arr, symb, initial_pos=0):
    pos = -1
    for i, elem in enumerate(arr):
        if str(elem) in symb and i >= initial_pos:
             pos = i
    return pos

def find_first_symbol(arr, symb, initial_pos=0):
    for i, elem in enumerate(arr):
        if str(elem) in symb and i >= initial_pos:
            return i
    return -1


def go2nums(arr):
    return [int(i) if i.isdigit() else i for i in arr]
