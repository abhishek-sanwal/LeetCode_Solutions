
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        mod = (10**9) + 7
        
        result = [0] * ((10**6))
        result[0] = 1
        
        for i in range(100005):
            
            result[i+zero] %= mod
            result[i+zero] += result[i]
            
            result[i+one] %= mod
            result[i+one] += result[i]
        
        s = 0
        
        for i in range(low,high+1):
            s = (s+result[i]) % mod
            
        return s