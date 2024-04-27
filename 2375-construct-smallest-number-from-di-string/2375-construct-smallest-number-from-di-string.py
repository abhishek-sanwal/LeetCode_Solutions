class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        lis = [str(i) for i in range(1,len(pattern)+2)]
        
        i = 0
        
        while i < len(pattern):
            
            if pattern[i] == 'D':
                start = i                
                while i < len(pattern) and pattern[i] == 'D':
                    i+=1
                    
                end = i
                while start < end:
                    lis[start], lis[end] = lis[end], lis[start]
                    start += 1
                    end -= 1 
                continue
            i+=1
        
        return "".join(lis)
        
        