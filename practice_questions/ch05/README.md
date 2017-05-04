# Chapter 5 – Dictionaries and Structuring Data

> Q: 1. What does the code for an empty dictionary look like?
`{}`

> Q: 2. What does a dictionary value with a key 'foo' and a value 42 look like?
`{'foo', 42}`

> Q: 3. What is the main difference between a dictionary and a list?
The item stored in dictionary are unordered, while the items in a list are ordered.

> Q: 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
`KeyError` error.

> Q: 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
no different.

> Q: 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
`'cat' in spam` checks whether there is a 'cat' key, while `'cat' in spam.values()` checks whether there is a 'cat' value.

> Q: 7. What is a shortcut for the following code?
>
>```py
>if 'color' not in spam:
>    spam['color'] = 'black'
>```

```py
spam.serdefault('color', 'black')
```

> Q: 8. What module and function can be used to “pretty print” dictionary values?
`pprint.pprint()`