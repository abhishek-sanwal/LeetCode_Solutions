class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        num_upper = num_lower = 0
        
        # 0(N)
        for i in word:
            
            if i.islower():
                
                bit = ord(i) - 97
                num_lower |= 1<<bit
            else:
                
                bit = ord(i) - 65
                num_upper |= 1<<bit
        count = 0
        for i in range(26):
            
            mask = 1<<i
            
            if  (num_lower & mask) and (num_upper & mask):
                
                count += 1
                
        return count
        
        
        
        
        
        # TC => 0(N + 26) => 0(N)
        # SC => 0(26*2) = 0(52) = 0(1)
        vis = set(word)
        
        count = 0
        
        for i in "abcdefghijklmnopqrstuvwxyz":
            
            if i in vis and i.upper() in vis:
                count += 1
        return count
        