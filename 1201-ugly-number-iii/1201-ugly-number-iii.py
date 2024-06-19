class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
        ab = a*b//gcd(a, b)
        bc = b*c//gcd(b, c)
        ca = c*a//gcd(c, a)
        abc = ab*c//gcd(ab, c)
        
        lo, hi = 1, n*min(a, b, c)
        while lo <= hi: 
            mid = lo + hi >> 1
            if mid//a + mid//b + mid//c - mid//ab - mid//bc - mid//ca + mid//abc < n:
                lo = mid + 1
            else:
                hi = mid - 1
                
        return lo 
        
        low = 0
        
        high = 10**18
        
        factos = [a,b,c]
        
        def lcm(a,b):
            
            return (a*b) // gcd(a,b)
        
        def lcm(*lis):
            
            return reduce(lcm,lis)
            
        
        while low <= high:
            
            mid = (low + high)//2
            
            count = mid//a + mid//b + mid//c - mid//lcm(a,b) - mid//lcm(a,c) - mid//lcm(b,c) + mid//lcm(a,b,c)
            
            if count >= n:
                
                high = mid - 1
                
            else:
                low = mid + 1
                
        return low
            
            