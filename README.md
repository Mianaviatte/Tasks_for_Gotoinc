# Tasks for Gotoinc 

Trainee Ruby on Rails Developer

1. Write a simple cipher code:
Take all even bits of the string and concatenate them with all odd n times. As a result, return the string.

Example:
("Abcdefghij", 1) -> "bdfhjacegi"
("Abcdefghij", 2) -> "bdfhjacegi" -> "dhaeibfjcg"

Write two methods / functions:
- encrypt (text, n)
- decrypt (encrypted_text, n)

For both methods:
If the input string is empty or NULL, return the input string value
If n <= 0, return the original value of the input string

2. Write a method / function that accepts text (take into account punctuation and special characters) and returns an array of the three most common words in the text in descending order.

- A word is a string of letters (A to Z) that optionally contains one or more apostrophes (')
- Matches must not be case sensitive and words in the returned array must be lowercase
- If the text contains less than three unique words, return an empty array
