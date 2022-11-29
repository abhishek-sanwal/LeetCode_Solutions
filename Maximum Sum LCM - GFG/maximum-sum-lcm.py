#User function Template for python3
from math import sqrt
class Solution:
    
    def factors(self,n):
        
        x = int(sqrt(n))+1
        
        s = 0
        
        for i in range(1,x):
            
            if n%i==0:
                
                s += i
                
            if i!=(n//i):
                
                if n%(n//i)==0:
                    s+=(n//i)
                    
        return s
                
        
    
    def maxSumLCM (self, n):
        
        if n==1:
            return 1
            
        return self.factors(n)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.maxSumLCM(n))
# } Driver Code Ends