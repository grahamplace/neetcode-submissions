class TrieNode:
    def __init__(self):
        self.word: bool = False
        self.children: dict[str, TrieNode] = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True

# trie = PrefixTree()
# trie.insert("ab")
# assert 'a' in trie.root.children
# assert 'b' in trie.root.children['a'].children
# assert trie.root.children['a'].children['b'].word
# assert trie.search("ab")
# assert trie.search("a") is False
# assert trie.search("abc") is False
# assert trie.startsWith("a")
# assert trie.startsWith("ab")
# assert trie.startsWith("abc") is False
        