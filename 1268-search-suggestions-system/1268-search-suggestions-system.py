
class TrieNode:
    
    def __init__(self):
        
        self.children = dict()
        self.isWord = False
        

class Trie:

    def __init__(self):
        
        self.trie = TrieNode()

    def insert(self,index:int, word: str) -> None:
        
        trie = self.trie
        
        for i in word:
            
            if i not in trie.children:
                
                trie.children[i] = TrieNode()

            trie = trie.children[i]
                
        trie.isWord = True
    
        
    def search(self,products:List[str], word: str) -> bool:
        
        ans = list()
        trie = self.trie
        lis = list()
        def dfs(index,trie,curr_word):
            
            if len(lis) == 3:
                
                return None
            
            if trie.isWord:
                lis.append(curr_word)
            
            for char in string.ascii_lowercase:
                
                if char in trie.children:
                    
                    dfs(index+1,trie.children[char],curr_word + char)
        pref = ""
        for char in word:
            pref += char
            if char not in trie.children:
                break
            trie = trie.children[char]
            dfs(0,trie,pref)
            ans.append(lis)
            lis = list()
        
        if len(ans) != len(word):

            for j in range(len(word)-len(ans)):
                
                ans.append(list())
        return ans
  
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        
        trie = Trie()
        
        for index, word in enumerate(products):
            
            trie.insert(index,word)
    
        return trie.search(products, searchWord)