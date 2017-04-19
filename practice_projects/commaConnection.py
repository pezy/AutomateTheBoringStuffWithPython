spam = ['apple', 'bananas', 'tofu', 'cats']

def list2Str(l):
    if not l:
        return ''
    if len(l) == 1:
        return l[0]
    s = ''
    for i in range(len(l) - 1):
        s += l[i] + ', '
    s += 'and ' + l[-1]
    return s

print(list2Str(spam))