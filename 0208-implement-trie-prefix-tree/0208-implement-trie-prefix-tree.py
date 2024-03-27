
class TrieNode:
    
    def __init__(self):
        
        self.children = dict()
        self.word = False

class Trie:

    def __init__(self):
        
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        
        trie = self.trie
        
        for i in word:
            
            if i not in trie.children:
                
                trie.children[i] = TrieNode()
                
            trie = trie.children[i]
            
        trie.word = True
            
    def search(self, word: str) -> bool:
        
        trie = self.trie
        
        for i in word:
            
            if i not in trie.children:
                
                return False
                
            trie = trie.children[i]
            
        return trie.word
        

    def startsWith(self, prefix: str) -> bool:
        
        word = prefix
        trie = self.trie
        
        for i in word:
            
            if i not in trie.children:
                
                return False
                
            trie = trie.children[i]
            
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)