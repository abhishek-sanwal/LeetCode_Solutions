class Solution:
    def maximum69Number (self, num: int) -> int:
        
        lis =[i for i in str(num)]
        
        for i,ele in enumerate(lis):
            
            if ele == "6":
                
                lis[i] ="9"
                
                break
                
        return "".join(lis)
                
            