# Autocomplete
This program efficiently returns a list of words that can complete a given
prefix.

## How to use it?
Run this command in the same directory as [autocomplete.py](autocomplete.py)
```
python3 autocomplete.py
```
The Trie (underlying data structure) will be created and then you will be
prompted to enter a prefix.


## How does it work?
The words are stored in a Retreival Tree, also known as a 
[Trie](https://en.wikipedia.org/wiki/Trie) (pronounced *try*). In a Trie
nodes contain letters. These nodes can have child nodes, representing more
letters. Nodes also contain a boolean value determining if that node is a
terminal node, in which case, the letters leading up to that node create a
word.

To find all ways to complete a prefix, walk the tree with the prefix's
letters. If at any point there is no existing node to complete the string,
you can infer there is no solution. Once you reach the last letter of the
prefix, you can recursively check all existing branches below the node,
and get all words that complete the prefix.

## Big O analysis
**Time Complexity:**  
The time complexity of adding a word or looking up a word is O(n), n being
the length of the word, because you have to either walk or create as many nodes
as there are letters in the word. Finding words is also linear, O(n), but n is
the sum of the lengths of all completed words. This is what makes them so
efficient.

**Space Complexity**  
The space complexity of Tries is where it suffers. Arrays or dictionaries
allocate extra memory than needed, and they are required to store node's
children. That means for every node, even if it only has one child, extra
space is allocated. The advantages though, are that there can be overlap
between letters, popular prefixes, like *pre* for instance. An imprevement is
to use [Compressed Tries](https://people.ok.ubc.ca/ylucet/DS/CompressedTrie.html).
They work by grouping many nodes with only one child together, until a split
occurs.

## See the code
[Autocomplete Code](autocomplete.py)