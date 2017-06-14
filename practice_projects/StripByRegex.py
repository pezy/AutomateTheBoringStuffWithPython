#! python3
'''
Regex Version of strip()

Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to strip,
then whitespace characters will be removed from the beginning and end of
the string. Otherwise, the characters specified in the second argument to
the function will be removed from the string.

'''

from re import compile


def stripInRegexWay(string, bad=" "):
    strip_regex = compile(r'(^[{0}]*)(.*?)([{1}]*$)'.format(bad, bad))
    return strip_regex.search(string).group(2)

assert stripInRegexWay('  dsadas  ') == 'dsadas'
assert stripInRegexWay(' dasd dsd  ') == 'dasd dsd'
assert stripInRegexWay('addsada', 'ad') == 's'
assert stripInRegexWay('adsradsnads', 'ads') == 'radsn'
