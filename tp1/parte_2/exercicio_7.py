class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

trie = Trie()
trie.insert("casa")
trie.insert("carro")
trie.insert("caminhão")
trie.insert("cachorro")
trie.insert("cadeira")

print(trie.search("casa"))  
print(trie.search("carro")) 
print(trie.search("caminhão"))
print(trie.search("cachorro"))  
print(trie.search("cadeira"))  
print(trie.search("cama"))

trie = Trie()

words = ["casa", "carro", "caminhão", "cachorro", "cadeira"]
for word in words:
    trie.insert(word)




