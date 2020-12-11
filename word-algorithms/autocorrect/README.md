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
