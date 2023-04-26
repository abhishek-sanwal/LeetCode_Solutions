class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        def reverse(n):
            
            sumi = 0
            
            while n:

                sumi = (sumi*10) + n%10
                
                n//=10
                
            return sumi
        
        lis = []
        
        for i in nums:

            for x in str(i):
                
                lis.append(ord(x)-48)
                
        return lis