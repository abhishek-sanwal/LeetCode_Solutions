from math import log2,ceil,floor
class Solution:
    def numberOfCuts(self, n: int) -> int:
        
        if n==1:
            return 0
        
        return n//2 if not n%2 else n
        