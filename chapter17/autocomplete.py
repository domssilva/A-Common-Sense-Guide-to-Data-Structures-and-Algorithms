from trie import Trie

trie = Trie()
trie.insert('ace')
trie.insert('bad')
trie.insert('cat')
trie.insert('can')

print(
    trie.collect_all_words()
)