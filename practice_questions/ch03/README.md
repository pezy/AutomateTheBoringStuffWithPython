# CHAPTER 3 - FUNCTIONS

> Q: 1. Why are functions advantageous to have in your programs?

A: Avoid duplicating codes.

> Q: 2. When does the code in a function execute: when the function is defined or when the function is called?

A: called.

> Q: 3. What statement creates a function?

A: `def` statements.

> Q: 4. What is the difference between a function and a function call?

A: A function consists of the def statement and the code in its `def` clause.

A function call is what moves the program execution into the function, and the function call evaluates to the  function's return value.

> Q: 5. How many global scopes are there in a Python program? How many local scopes?

A: Just one global scope, and a local scope is created whenever a function is called.

> Q: 6. What happens to variables in a local scope when the function call returns?

A: destroyed.

> Q: 7. What is a return value? Can a return value be part of an expression?

A: return value is the result of a function call. Return value can be part of an expression.

> Q: 8. If a function does not have a return statement, what is the return value of a call to that function?

A: `None`.

> Q: 9. How can you force a variable in a function to refer to the global variable?

A: `global` statement.

> Q: 10. What is the data type of None?

A: `NoneType`

> Q: 11. What does the import `areallyourpetsnamederic ` statement do?

A: import a module named `areallyourpetsnamederic `.

> Q: 12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?

A: `spam.bacon()`

> Q: 13. How can you prevent a program from crashing when it gets an error?

A: use `try...except...`

> Q: 14. What goes in the try clause? What goes in the except clause?

A: potential error goes in the `try` clause, then if the error happens, goes in the `except` clause.

---

## Practice Projects

see [collatz.py](collatz.py)