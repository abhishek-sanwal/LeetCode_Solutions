class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
        ab = a*b//gcd(a, b)
        bc = b*c//gcd(b, c)
        ca = c*a//gcd(c, a)
        abc = ab*c//gcd(ab, c)
        
        low = 0
        
        high = n*min(a,b,c)
        
        while low <= high:
            
            mid = (low + high)//2
            
            count = mid//a + mid//b + mid//c - mid//ab- mid//bc- mid//ca + mid//abc
            
            if count >= n:
                
                high = mid - 1
                
            else:
                low = mid + 1
                
        return low
            
            