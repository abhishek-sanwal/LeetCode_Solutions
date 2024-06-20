
class TrieNode:
    
    def __init__(self):
        
        self.children = dict()
        self.word = False
        self.wordsIndex = list()

class Trie:

    def __init__(self):
        
        self.trie = TrieNode()

    def insert(self,index:int, word: str) -> None:
        
        trie = self.trie
        
        for i in word:
            
            if i not in trie.children:
                
                trie.children[i] = TrieNode()

            trie = trie.children[i]
            trie.wordsIndex.append(index)
                
        trie.word = True
            
    def search(self,products:List[str], word: str) -> bool:
        
        trie = self.trie
        lis = []
        for i in word:
            
            if i not in trie.children:
                
                lis.append([])
                break
                
            trie = trie.children[i]
            
            curr_suggestion = list()
            for j in trie.wordsIndex:
                curr_suggestion.append(products[j])
                if len(curr_suggestion) == 3:
                    break
            lis.append(curr_suggestion)
        if len(lis) != len(word):
            
            for j in range(len(word)-len(lis)):
                
                lis.append([])
        
        return lis
        

  
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        
        trie = Trie()
        
        for index, word in enumerate(products):
            
            trie.insert(index,word)
    
        return trie.search(products, searchWord)