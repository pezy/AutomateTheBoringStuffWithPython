#! python3

'''
Strong Password Detection

Write a function that uses regular expressions to make sure the password string
it is passed is strong. A strong password is defined as one that is at least
eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against
multiple regex patterns to validate its strength.
'''

import re


def checkPasswordSecurity(passwd):
    if len(passwd) < 8:
        print("A strong password is at least eight characters long")
        return False

    uppercase_regex = re.compile(r'[A-Z]+')
    lowercase_regex = re.compile(r'[a-z]+')
    digit_regex = re.compile(r'\d+')

    if uppercase_regex.search(passwd) is None:
        print("A strong password should contains uppercase characters")
        return False

    if lowercase_regex.search(passwd) is None:
        print("A strong password should contains lowercase characters")
        return False

    if digit_regex.search(passwd) is None:
        print("A strong password has at least one digit")
        return False

    return True

assert checkPasswordSecurity('Abc123') is False
assert checkPasswordSecurity('ewqeqw32') is False
assert checkPasswordSecurity('HUIH54DSD') is False
assert checkPasswordSecurity('dadasDEDEDE') is False
assert checkPasswordSecurity('Ddsdad8678') is True
