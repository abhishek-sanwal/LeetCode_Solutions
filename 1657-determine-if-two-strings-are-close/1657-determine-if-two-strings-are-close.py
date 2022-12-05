
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            
            return False
        
        x = Counter(word1)
        y = Counter(word2)
        
        if len(x) != len(y):
            return False
        
        for i in x:
            if i not in y:
                return False
            
        arr1 = list(x.values())
        
        arr2 = list(y.values())
        
        arr1.sort()
        arr2.sort()
        
        for i in range(len(arr1)):
            
            if arr1[i] != arr2[i]:
                
                return False
            
        return True
            
            