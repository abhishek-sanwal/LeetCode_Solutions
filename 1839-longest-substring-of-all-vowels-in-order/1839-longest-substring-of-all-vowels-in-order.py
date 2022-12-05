class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        check = set()
        
        curr_len = max_len = 0
        curr_idx = -1
        vowels = ["a","e","i","o","u"]
        
        for i in range(len(word)):
            
            if word[i] in vowels:
                
                if ord(word[i])-97 >= curr_idx:
                
                    curr_idx = ord(word[i]) -97
                    
                    check.add(word[i])
                    curr_len += 1
                    
                else:
                    check = set()
                    check.add(word[i])
                    curr_idx = ord(word[i])-97
                    curr_len = 1
                    
            if len(check) == 5:
                max_len = max(max_len,curr_len)
                
        return max_len
                
                
                
                