def collatz(x):
    if x % 2 == 0:
        x = x // 2
    else:
        x = 3 * x + 1
    print(x)
    return x

def getInput():
    try:
        return int(input())
    except (ValueError, NameError):
        print('Your should input an integer.')
        return getInput()

n = getInput()
if n == 0:
    print('It would enter an infinite loop.')
else:
    while n != 1:
        n = collatz(n)
    