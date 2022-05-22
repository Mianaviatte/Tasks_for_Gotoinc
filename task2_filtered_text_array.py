# Write a method / function that accepts text (take into account punctuation and special characters) 
# and returns an array of the three most common words in the text in descending order.
# A word is a string of letters (A to Z) that optionally contains one or more apostrophes (')
# Matches must not be case sensitive and words in the returned array must be lowercase
# If the text contains less than three unique words, return an empty array.

from collections import Counter
from operator import itemgetter
import re

def common_word(filename):

    # Input with lorem ipsum document opened for reading
    with open(filename) as text_sample:
        texts = text_sample.read()

        # Lowering case & filtering out numbers, punctuation and special characters except apostrophes (')
        re.sub(r'[A-Za-zÀ-ÿ \']', '', texts)
        texts = re.sub(r'[-()\"#/@;:<>{}`+=~|.!?,\n]', '', texts.lower())
        
        # Splitting word by word and saving as a list.
        words = texts.split(' ')

        # Collect a dict with keys = common words and values = amount of them on text, then order by amount
        lorem_count = {word: words.count(word) for word in set(words)}
        sorted_lorem_count = sorted(lorem_count.items(), key=itemgetter(1), reverse=True)
        
        # If dict is less then 3 items long, return an empty array. 
        # If not - return a list of keys, where values are greatest.
        results = [] if len(lorem_count)<3 else [*sorted_lorem_count]
        results = results[:3]

        # ALTERNATIVE TO LINES 27-34:
        # results = [] if len(set(words))<3 else Counter(words).most_common(3)

    print(results)

common_word('lorem_ipsum.txt')
common_word('nothing.txt')