class Node:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current_node = self.root
        # iterate over input
        for char in word:
            if current_node.children.get(char):
                # follow the child node
                current_node = current_node.children[char]
            else:
                # insert new node
                new_node = Node()
                current_node.children[char] = new_node
                # follow new node
                current_node = new_node
        # after the whole word is inserted into the trie,
        # add a '*' to establish the end of the word
        current_node.children['*'] = None

    def search(self, word):
        current_node = self.root
        # iterate over input
        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                """
                current character couldn't be found
                this means it's not possible to have the word
                we're searching for in this trie
                """
                return None
        return current_node

    # Page 320 example
    def collect_all_words(self, node=None, word="", words=[]):
        current_node = node or self.root
        # traverse trie
        for key, child_node in current_node.children.items():
            if key == '*':
                words.append(word)
            else:
                self.collect_all_words(child_node, word + key, words)
        return words


trie = Trie()
trie.insert('ace')
trie.insert('bad')
trie.insert('cat')

# print('search bad:', trie.search('bad'))
# print('search bat:', trie.search('bat'))