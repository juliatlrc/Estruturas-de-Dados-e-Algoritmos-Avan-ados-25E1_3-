# Exercício 9: Inserção e Busca em Trie
print("Exercício 9: Inserção e Busca em Trie")

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
trie.insert("apple")
print(trie.search("apple"))  # True
print(trie.search("app"))    # False


# Exercício 10: Aplicação de Trie
print("\nExercício 10: Aplicação de Trie")

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

    def search_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._get_words_with_prefix(node, prefix)

    def _get_words_with_prefix(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child in node.children.items():
            words.extend(self._get_words_with_prefix(child, prefix + char))
        return words


trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")
trie.insert("bat")
trie.insert("batman")
print(trie.search_with_prefix("ba"))  # ['banana', 'bat', 'batman']


# Exercício 11: Comparação entre as Estruturas Heap e Trie
print("\nExercício 11: Comparação entre as Estruturas Heap e Trie")

print("Heap: eficiente para operações de fila de prioridade, inserção e remoção de elementos com base na prioridade.")
print("Trie: eficiente para operações de busca de prefixos e autocompletar palavras. A Trie é ideal quando trabalhamos com strings ou palavras.")


# Exercício 12: Casos de Uso da Estrutura de Dados Trie
print("\nExercício 12: Casos de Uso da Estrutura de Dados Trie")

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

    def search_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._get_words_with_prefix(node, prefix)

    def _get_words_with_prefix(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child in node.children.items():
            words.extend(self._get_words_with_prefix(child, prefix + char))
        return words


trie = Trie()
words = ["apple", "app", "banana", "bat", "batman", "ball"]
for word in words:
    trie.insert(word)

print(trie.search_with_prefix("ba"))  # ['banana', 'bat', 'batman', 'ball']

