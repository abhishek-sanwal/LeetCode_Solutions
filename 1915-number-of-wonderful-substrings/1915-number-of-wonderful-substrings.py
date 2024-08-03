class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        
        
        odd_mask =  ans = 0
        
        mapp = defaultdict(int)
        mapp[0] = 1
        
        for char in word:
            
            bit = ord(char) - 97
            
            odd_mask ^= (1 << bit)
            
            ans += mapp[odd_mask]
            
            mapp[odd_mask] += 1
            
            for char in range(0,10):

                if odd_mask ^ (1<<char) in mapp:

                    ans += mapp[odd_mask^(1<<char)]
                
        return ans
        
        