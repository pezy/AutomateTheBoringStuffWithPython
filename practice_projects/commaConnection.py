#! python3
'''test for list_to_str'''

SPAM = ['apple', 'bananas', 'tofu', 'cats']


def list_to_str(lst):
    '''show list in string format'''
    if not lst:
        return ''
    if len(lst) == 1:
        return lst[0]
    ret = ''
    for i in range(len(lst) - 1):
        ret += lst[i] + ', '
    ret += 'and ' + lst[-1]
    return ret

print(list_to_str(SPAM))
