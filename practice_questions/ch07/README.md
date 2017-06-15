# Chapter 7 – Pattern Matching with Regular Expressions

> Q: 1. What is the function that creates Regex objects?

`re.compile()`

> Q: 2. Why are raw strings often used when creating Regex objects?

Because the backslashes don't have to be escaped.

> Q: 3. What does the search() method return?

`Match` objects

> Q: 4. How do you get the actual strings that match the pattern from a Match object?

`gourp()`

> Q: 5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

group 0 covers the entire. group 1 covers the first set of parentheses, and group 2 covers the second set of parentheses.

> Q: 6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

`\(`, `\)`, `\.`

> Q: 7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

group's number

> Q: 8. What does the | character signify in regular expressions?

or

> Q: 9. What two things does the ? character signify in regular expressions?

1. match zero or one of the preceding group
1. signify nongreedy matching

> Q: 10. What is the difference between the + and * characters in regular expressions?

`+` matches **one** or more, `*` matches **zero** or more.

> Q: 11. What is the difference between {3} and {3,5} in regular expressions?

`{3}` matches exactly 3 instance of the preceding group, {3, 5} matches between 3 ~ 5 instances.

> Q: 12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?

single digit, word, or space character respecitively.

> Q: 13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?

single character that is not a digit, word, or space character, respecitively.

> Q: 14. How do you make a regular expression case-insensitive?

`re.I` or `re.IGNORECASE`

> Q: 15. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?

`.` matches any character except the newline character. If `re.DOTALL` is passed as the second argument, the dot will also match newline characters.

> Q: 16. What is the difference between these two: .* and .*?

greedy match and nongreedy match.

> Q: 17. What is the character class syntax to match all numbers and lowercase letters?

`[0-9a-z]`

> Q: 18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

'X drummers, X pipers, five rings, X hens'

> Q: 19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

`re.VERBOSE` allows you to add whitespace and comments to the string passed to `re.compile()`.

> Q: 20. How would you write a regex that matches a number with commas for every three digits? It must match the following:
> '42'
> '1,234'
> '6,368,745'
> but not the following:
> '12,34,567' (which has only two digits between the commas)
> '1234' (which lacks commas)

`^\d{1,3}(,\d{3})*$`

> Q: 21. How would you write a regex that matches the full name of someone whose last name is Nakamoto? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
> 'Satoshi Nakamoto'
> 'Alice Nakamoto'
> 'Robocop Nakamoto'
> but not the following:
> 'satoshi Nakamoto' (where the first name is not capitalized)
> 'Mr. Nakamoto' (where the preceding word has a nonletter character)
> 'Nakamoto' (which has no first name)
> 'Satoshi nakamoto' (where Nakamoto is not capitalized)

`^[A-Z][a-z]]*\sNakamoto$`

> Q: 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
> 'Alice eats apples.'
> 'Bob pets cats.'
> 'Carol throws baseballs.'
> 'Alice throws Apples.'
> 'BOB EATS CATS.'
> but not the following:
> 'Robocop eats apples.'
> 'ALICE THROWS FOOTBALLS.'
> 'Carol eats 7 cats.'

`re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)`