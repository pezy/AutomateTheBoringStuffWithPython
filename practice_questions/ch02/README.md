# CHAPTER 2 - FLOW CONTROL

> Q: 1. What are the two values of the Boolean data type? How do you write them?

A: True, False

> Q: 2. What are the three Boolean operators?

A: and, or, not

> Q: 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

| combination     | value |
| --------------- | ----- |
| True and True   | True  |
| True and False  | False |
| False and True  | False |
| False and False | False |
| True or True    | True  |
| True or False   | True  |
| False or True   | True  |
| False or False  | False |
| not True        | False |
| not False       | True  |

> Q: 4. What do the following expressions evaluate to?

```python
(5 > 4) and (3 == 5) # False
not (5 > 4) # False
(5 > 4) or (3 == 5) # True
not ((5 > 4) or (3 == 5)) # not (True or False) => False
(True and True) and (True == False) # True and False => False
(not False) or (not True) # True or False => True
```

> Q: 5. What are the six comparison operators?

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not equal to             |
| <        | Less than                |
| >        | Greater than             |
| <=       | Less than or equal to    |
| >=       | Greater than or equal to |

> Q: 6. What is the difference between the equal to operator and the assignment operator?

A: `==` asks whether two values are the same as each other; `=` puts the value on the right into the variable on the left.

> Q: 7. Explain what a condition is and where you would use one.

A: Condition is the boolean expressions. You can use it in `if...elif...else`, `while`, `for` statements.

> Q: 8. Identify the three blocks in this code:

```python
spam = 0 #1
if spam == 10: #1
    print('eggs') #2
    if spam > 5: #2
        print('bacon') #3
    else: #2
        print('ham') #3
    print('spam') #2
print('spam') #1
```

> Q: 9. Write code that prints Hello if 1 is stored in `spam`, prints Howdy if 2 is stored in `spam`, and prints Greetings! if anything else is stored in `spam`.

A: [](condition.py)

> Q: 10. What can you press if your program is stuck in an infinite loop?

A: `Ctrl-C`

> Q: 11. What is the difference between `break` and `continue`?

A: `break` can exit loop clause immediately, `continue` just jumps back to the start of the loop and reevaluates the loop's condition.

> Q: 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

A:  same.

> Q: 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

A: [](loop.py)

> Q: 14. If you had a function named bacon() inside a module named `spam`, how would you call it after importing `spam`?

A: `spam.bacon()`

> Extra credit: Look up the round() and abs() functions on the Internet, and find out what they do. Experiment with them in the interactive shell.

A: [](extra.py)