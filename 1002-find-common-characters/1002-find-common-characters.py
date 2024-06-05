class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        x = Counter(words[0])
        
        for word in words:
            
            x &= Counter(word)
        
        lis = list()
        
        for key in x:
            
            for i in range(x[key]):
                
                lis.append(key)
            
        return lis
        
        
        candidates = mapp()
        
        for char in words[0]:
            
            candidates.add(char)
            
        
        for i in range(1,len(words)):
            
            remove = set()
            
            for char in candidates:
                
                if words[i].count(char) == 0:
                    
                    remove.add(char)
                    
            for char in remove:
                candidates.remove(char)
            
        return "".join(candidates)
        
        
        chars = [False]*26
        
        for char in words:
            
            chars[ord(char) - ord('a')] = True
            
        # Iterate over all words
        
        for i in range(len(words)):
            
            for char in words:
                
                x = ord(char) - ord('a')
                
                if chars[x]:
                    pass
            
            
        