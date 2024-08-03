class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        
        # Prefix odd mask reprsents which char occurs even times and which occurs odd times using bits. 0 means even 1 means odd
        
        
        prefix_odd_mask =  ans = 0
        
        mapp = defaultdict(int)
        
        mapp[0] = 1
        
        for char in word:
            
            bit = ord(char) - 97
            
            # whenever a new character occurs we are setting that bit i.e. increasing frequency.
            
            # since xor handles addition and substraction under modulo 2. We are doing xor
            prefix_odd_mask ^= (1 << bit)
            
            # Find similar bit patterns i.e. count number of substrings with all characters present in even frequency.
            # if prefix [0...j] is equal to prefix[0..i] all bits are same that means all prefix[i..j] contains all charactes in even frequency
            ans += mapp[prefix_odd_mask]
            
            mapp[prefix_odd_mask] += 1
            
            # a to j
            for char in range(0,10):
                
                # we can have atmost one odd char and we need to count them
                # toggle each char bit in check wheather it is avaible in mapp then add it
                odd_freq_char_mask = prefix_odd_mask ^ (1 << char)
                ans += mapp[odd_freq_char_mask]
                    
        return ans
        
        