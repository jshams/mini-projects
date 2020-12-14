# Autocorrect

Autocorrect is a feature used by almost everyone daily. It's a seemless feature
when we see it, but the algorithm behind it is not as simple as it seems.
It is often confused with autocomplete, a much simpler problem taught in almost
all advanced CS courses. So what makes autocorrect so complex? Why do CS
professors tend to avoid it within their lectures? Here I will show two
methods for autocorrect. Neither are _fast_, though I will discuss where they
can be improved.

## Incomplete

This project is one of my newer mini-projects. That said I am still working
on this README. Sections followed by elipses (...) are yet to be completed.

## Method 1 - BK Trees

The first method is the most common. It has the most flexibility for
improvements and, at its core, is the same method used by Google Search and
your smartphone.

This method utilizes BK Trees. A fairly uncommon tree used mainly for this
purpose. The tree's nodes store words and its child words. The children are
stored by distance. This makes searching through the tree fast.

...

## Method 2 - Outbound Autocorrect

The outbound approach is one that I came up with myself. There are cases where
it can be faster than that of the BK Tree, but in most cases can be considered
an impractical solution.

The outbound approach for autocomplete works by storing a set of all word
for fast lookup. A set of edits are performed using a BFS style. 1 edit at
a time. When a layer of edits leads to an existing word, all real words
found in that layer are returned.

...

## Code samples for correct

### Creating an instance of BKTree

```python
>>> words = ['melon', 'lemon', 'salmon']
>>> # create a BKTree instance filled with the words above
>>> autocorrect = BKTree(words)
```

### Creating an instance of OutboundAutocorrect

```python
>>> words = ['melon', 'lemon', 'salmon']
>>> # create a BKTree instance filled with the words above
>>> autocorrect = OutboundAutocorrect(words)
```

### Searching for corrections

Note the `correct` methods are the same for both of the above classes.

`correct` returns two items in a tuple. The first is a list of possible
corrections and the second is their distance from the typo word.

```python
>>> # search for a correction for 'lamon'
>>> autocorrect.correct('lamon')
(['lemon'], 1)
>>> autocorrect.correct('slamon')
(['lemon', 'salmon'], 2)
```

### Existing words

If the word exists, an array with the word along with a dist of 0 is returned.

```python
>>> autocorrect.correct('lemon')
(['lemon'], 0)
```

### Tollerance

The correct method has a default parameter called `tollerance`. This is the
maximum distance word to search for. Lower tollerance will result in better
performance. The default value is 3.

```python
>>> autocorrect.correct('slamon', tollerance=1)
([], 1)
>>> autocorrect.correct('slamon', tollerance=2)
(['lemon', 'salmon'], 2)
```

### No words found

In the case that no words are found, an empty array along with the tollerance
is returned.

```python
>>> autocorrect.correct('orange', tollerance=3)
([], 3)
```

## String distance

To better understand the complexities of this problem it is important to first
understand how distance is calculated between two words. String distance itself
is a complex problem and requires Dynamic Programming. See how string distance
is calculated in this mini project -
[Levenshtein Distance](../levenshtein-distance). This metric is used to
determine distance by the BK Tree.

## Comparing Methods

Discuss where either method is appropriate.

Notes:
Bk trees work better for smaller corpuses of text.
Outbound works best when the typo is close it's correction.

...

## Improving the BK Tree

...

## Resources

[BK Tree Introduction Implementation](https://www.geeksforgeeks.org/bk-tree-introduction-implementation/)
by Geeks for Geeks.

[The BK-Tree – A Data Structure for Spell Checking](https://nullwords.wordpress.com/2013/03/13/the-bk-tree-a-data-structure-for-spell-checking/)
by Xenopax's Blog.
