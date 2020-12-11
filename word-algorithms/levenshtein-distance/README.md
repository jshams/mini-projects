# Levenshtein Distance

Levenshtein distance, also known as Edit Distance, is a string algorithm used
to determine the distance between two strings. This is the number of **Edits**
to get from one string to the other.

## Edits

An **edit** is defined as an _insertion_, _deletion_, or a _replacement_.
Some implementations also count swaps as a single edit.
And others define a replacement as 2 edits (1 delete + 1 insert).
For this implementation, the three mentioned above all count as 1 edit.

## Solve using Dynamic Programming

Leveshtein distance is a Dynamic Programming problem solved untraditionally.
Most DP problems are seen using a hash map to store answers to previous
_sub-problems_. In the case of Levenshtein, we use a 2D matrix instead.
To solve Levenshtein for 2 strings, first find the distance between their
prefixes, and recurse. This is where the overlap occurs. Instead of recursing
a matrix can be used to map solutions to prefixes. See this gif filling in the
matrix for the words "real" and "tree".

<img height="200" src="https://media.giphy.com/media/BznRv4VWWtlUn0YmbW/giphy.gif">

<a href="https://giphy.com/embed/BznRv4VWWtlUn0YmbW">via GIPHY</a>

## Code Samples

Finding the distance between 2 strings

```python
>>> string1 = 'real'
>>> string2 = 'tree'
>>> levenshtein(string1, string2)
3
>>> string1 = 'aleph bet'
>>> string2 = 'alphabet'
>>> levenshtein(string1, string2)
3
```

Using default param `display_solution`. When `display_solution=True` the
solution and the edit steps will be printed to the console. The steps are
calculated using a helper function I call `reversenshtein`.

```python
>>> string1 = 'real'
>>> string2 = 'tree'
>>> ans = levenshtein(string1, string2, display_solution=True)
Edit "real" -> "tree"

      r  e  a  l
  [0, 1, 2, 3, 4]
t [1, 1, 2, 3, 4]
r [2, 1, 2, 3, 4]
e [3, 2, 1, 2, 3]
e [4, 3, 2, 2, 3]

Number of operations: 3
Edit operations:
        Replace the char "l", at index 3, with "e"
                "real" -> "reae"
        Delete the char "a" at index 2
                "reae" -> "ree"
        Insert the char "t" at index 0
                "ree" -> "tree"
>>> ans
3
```

## View the code

See the code [here](levenshtein.py).
