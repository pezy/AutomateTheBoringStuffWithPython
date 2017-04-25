# CHAPTER 4 - LISTS



> Q: 1. What is []?

A: empty list.

> Q: 2. How would you assign the value 'hello' as the third value in a list stored in a variable named `spam`? (Assume `spam` contains [2, 4, 6, 8, 10].)

A: `spam[2] = 'hello'`

> Q: For the following three questions, let’s say `spam` contains the list ['a', 'b', 'c', 'd'].
> Q: 3. What does `spam[int(int('3' * 2) // 11)]` evaluate to?

A: 'd'

> Q: 4. What does `spam[-1]` evaluate to?

A: 'd'

> Q: 5. What does `spam[:2]` evaluate to?

A: '['a', 'b']'

> Q: For the following three questions, let’s say `bacon` contains the list [3.14, 'cat', 11, 'cat', True].
> Q: 6. What does `bacon.index('cat')` evaluate to?

A: 1

> Q: 7. What does `bacon.append(99)` make the list value in bacon look like?

A: [3.14, 'cat', 11, 'cat', True, 99]

> Q: 8. What does bacon.remove('cat') make the list value in bacon look like?

A: [3.14, 11, 'cat', True]

> Q: 9. What are the operators for list concatenation and list replication?

A: `+` and `*`

> Q: 10. What is the difference between the append() and insert() list methods?

A: `append` only to the end, `insert` can everywhere.

> Q: 11. What are two ways to remove values from a list?

A: `remove` and `del`

> Q: 12. Name a few ways that list values are similar to string values.

A: Both lists and strings can be passed to `len()`, have indexes and slices, be used in `for` loops, be concatenated or replicated, and be used with the `in` and `not in` operators.

> Q: 13. What is the difference between lists and tuples?

A: lists are mutable, tuples are immutable.

> Q: 14. How do you type the tuple value that has just the integer value 42 in it?

A: (42, )

> Q: 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

A: `tuple()` and `list()`

> Q: 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

A: references.

> Q: 17. What is the difference between `copy.copy()` and `copy.deepcopy()`?

A: The `copy.copy()` will do a shadow copy of list, while the `copy.deepcopy()` will do a deep copy of a list. Thus, `copy.deepcopy()` will duplicate any lists inside the list.

