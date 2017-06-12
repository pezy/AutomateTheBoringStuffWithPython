#! python3
"""Calculate collatz function"""

def collatz(x_value):
    '''collatz calculation'''
    if x_value % 2 == 0:
        x_value = x_value // 2
    else:
        x_value = 3 * x_value + 1
    print(x_value)
    return x_value

def get_input():
    '''get custom input'''
    try:
        return int(input())
    except (ValueError, NameError):
        print('Your should input an integer.')
        return get_input()

N = get_input()

if N == 0:
    print('It would enter an infinite loop.')
else:
    while N != 1:
        N = collatz(N)
print(N)
