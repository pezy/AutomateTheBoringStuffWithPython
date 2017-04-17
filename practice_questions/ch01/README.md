# CHAPTER 1 - PYTHON BASICS

> Q: 1. Which of the following are operators, and which are values?

```python
* #operator
'hello' #value
-88.8 #value
- #operator
/ #operator
+ #operator
5 #value
```

> Q: 2. Which of the following is a variable, and which is a string?

```python
spam #variable
'spam' #string
```

> Q: 3. Name three data types.

A: string, integer, float-point.

> Q: 4. What is an expression made up of? What do all expressions do?

A: Expression is values combined with operators. They always evaluate down to a single value.

> Q: 5. This chapter introduced assignment statements, like `spam = 10`. What is the difference between an expression and a statement?

A: [expressions are statements as well, but they only contain identifiers, literals and operators, and can be reduced to a single value.](http://stackoverflow.com/a/4728147/1155235)

> Q: 6. What does the variable bacon contain after the following code runs?

```python
bacon = 20
bacon + 1
```

A: 20

> Q: 7. What should the following two expressions evaluate to?

```python
'spam' + 'spamspam' #'spamspamspam'
'spam' * 3 # 'spamspamspam'
```

> Q: 8. Why is eggs a valid variable name while 100 is invalid?

A: Because 100 is value.

> Q: 9. What three functions can be used to get the integer, floating-point number, or string version of a value?

A: `int()`, `float()`, `str()`.

> Q: 10. Why does this expression cause an error? How can you fix it?

```python
'I have eaten ' + 99 + ' burritos.'
```

A: Because Adding an integer to a string is ungrammatical in python. You can fixed this by using a string version of 99, like following:

```python
'I have eaten ' + str(99) + ' burritos.'
```