class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        
        
        prefix_odd_mask =  ans = 0
        
        mapp = defaultdict(int)
        
        mapp[0] = 1
        
        for char in word:
            
            bit = ord(char) - 97
            
            prefix_odd_mask ^= (1 << bit)
            
            ans += mapp[prefix_odd_mask]
            
            mapp[prefix_odd_mask] += 1
            
            # a to j
            for char in range(0,10):
                
                odd_freq_char_mask = prefix_odd_mask ^ (1 << char)
                
                if odd_freq_char_mask in mapp:
                    ans += mapp[odd_freq_char_mask]
        return ans
        
        