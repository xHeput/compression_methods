# This code use Shannon Fano Coding in order to compress word 
# basicly this method uses 5 step process which is:
# LIST -> SORT -> DIVIDE -> LABEL -> REPEAT
import collections


def create_list(message):
    # list keeps letters frequency
    list_ = dict(collections.Counter(message))

    # descending order
    list_sorted = sorted(list_.items(), key=lambda (k, v): (v, k), reverse=True)

    #format list [letter, frequency, code]
    final_list = []
    for key, value in list_sorted:
        final_list.append([key, value, ''])

    return final_list


def divide_list(list_):
    if len(list_) == 2:
        return [list_[0]], [list_[1]]
    else:
        n = 0
        for i in list_:
            n += i[1]
        x = 0
        distance = abs(2 * x - n)
        j = 0
        for i in xrange(len(list_)):
            x += list_[i][1]
            if distance < abs(2 * x - n):
                j = i
    return list_[0:j + 1], list_[j + 1 :]


def label_list(list_):
    code_book=[]
    l1, l2 = divide_list(list_)
    for i in l1:
        i[2] += '0'
        code_book[i[0]] = i[2]
    for i in l2:
        i[2] += '1'
        code_book[i[0]] = i[2]
    print ("Label Iter - ", code_book)
    if len(l1) == 1 and len(l2) == 1:
        return
    label_list(l2)
    return code_book

create_list("mississippi")
