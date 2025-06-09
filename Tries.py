class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    # Search full word
    def search(self, word):
        node = self._search_prefix(word)
        return node is not None and node.is_end

    # Check if any word starts with the prefix
    def starts_with(self, prefix):
        return self._search_prefix(prefix) is not None

    def _search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
