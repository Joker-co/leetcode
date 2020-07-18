class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        a = self.dic
        for i in word:
            if i not in a:
                a[i] = {}
            a = a[i]
        a['end'] = 1
                

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        a = self.dic
        for i in word:
            if i not in a:
                return False
            a = a[i]
        return 'end' in a


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        a = self.dic
        for i in prefix:
            if i not in a:
                return False
            a = a[i]
        return True
