class Solution:
    def countAndSay(self, n: int) -> str:
        
        def rle(s):
            
            lis = []
            
            i = 0
            
            while i < len(s):
                
                curr = s[i]
                count = 0
                while i< len(s) and s[i] == curr:
                    
                    i += 1
                    count += 1
                # print(count,curr)
                lis.append(str(count))
                lis.append(curr)
            # print(lis)
            return "".join(lis)
                    
        
        s = "1"
        
        for i in range(1,n):
            
            s = rle(s)
            
        return s