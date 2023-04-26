class Solution:
    def minimumSum(self, num: int) -> int:
        
        lis = []
        
        while num:
            
            lis.append(num%10)
            
            num//=10
        
        lis.sort()
        #print(lis)
        
        return ((lis[0] * 10) + lis[3]) + ((lis[1]*10)+lis[2])