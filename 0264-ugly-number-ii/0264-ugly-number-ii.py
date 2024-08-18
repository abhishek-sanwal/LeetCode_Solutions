from heapq import *

class Solution(object):
    
    def prime(self,n):
        
        if n<3:
            
            return True
        
        # x = int(n**0.5) + 1
        
        for i in range(2,n+1):
            
            if n % i == 0:
            
                if i not in {2,3,5}:
                    return False
                
                while n % i == 0:
                    
                    n //= i
                    
                
        return True
        
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [1]
        
        factors = [2,3,5]
        
        two_ptr = three_ptr = five_ptr = 0
        
        for i in range(1,n):
            
            num = min(dp[two_ptr]*2 ,dp[three_ptr]*3, dp[five_ptr]*5)
            dp.append(num)
            if num  == dp[two_ptr]*2:

                two_ptr += 1
                
            if num == dp[three_ptr]*3:
                
                three_ptr += 1
                
            if num == dp[five_ptr]*5:
                
                five_ptr += 1
        print(dp)    
        return dp[-1]
            
            
            
            
            
            
            
        return dp[-1]
        
    
#         heap = []
        
#         check = set([1])
        
#         heappush(heap,1)
        
#         while n:
            
#             x = heappop(heap)
            
#             if x*2 not in check:
            
#                 heappush(heap,x*2)  
#                 check.add(x*2)
            
#             if x*3 not in check:
            
#                 heappush(heap,x*3)  
#                 check.add(x*3)
                
#             if x*5 not in check:
            
#                 heappush(heap,x*5)  
#                 check.add(x*5)
#             n -= 1
            
#         return x
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        k = 10**7
        
        count = 0
        
        for i in range(1,k):

            if self.prime(i):
                count += 1
                
            if count == n:
                
                return i
        