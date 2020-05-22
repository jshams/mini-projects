# Anagram Generator
Anagrams are words that can be spelled with the same letters. This program
was created to generate new anagrams from a word.

## How does it work?
This anagram generator works by storing all words in a dictionary, where the
keys are sorted letters, and the values are a list of words that can be created
from the sorted letters.

## Big O analysis
**Creating the Anagram structure:**  
This takes O(nlogn) time because each word can be added
in O(1) time, but they must be sorted taking O(nlogn) time.  
**Finding the anagrams of a word:**  
Finding the anagram takes O(logn) time because the word must be sorted taking
O(nlogn) time then constant time to look up the word in the histogram.

## Implementation:
[anagrams.py](anagrams.py)