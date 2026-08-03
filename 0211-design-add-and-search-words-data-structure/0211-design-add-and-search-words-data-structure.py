class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            # base case: consumed entire word
            if i == len(word):
                return node.end_of_word

            c = word[i]
            if c == ".":
                # try every possible child at this position
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c], i + 1)

        return dfs(self.root, 0)