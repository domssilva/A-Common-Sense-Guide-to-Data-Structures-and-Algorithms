# Trie

- incredibly efficient
- O(K) where K is the size of the input

### O(K)

Expressing trie search in terms of big O is tricky. We can't quite call it O(1) neither O(N).
O(N) is misleading since N normally refers to the total amount of data stored in the data structure.

Most references have decided to call this O(K). Our trie can grow tremendously, but that will have no effect on the speed of our search.  
An O(K) algorithm on a string of 3 characters will always take 3 steps, no matter how large the trie is.
