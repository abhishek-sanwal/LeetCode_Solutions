class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = []
        lis = []
        
        for i,ele in enumerate(s):
            
            if ele ==")":
                
                if stack:
                    stack.pop()
                
                elif lis:
                    lis.pop()
                    
                else:
                    return False
                
            elif ele == "*":
                lis.append(i)
                
            else:
                stack.append(i)
                
        while stack and lis and stack[-1] < lis[-1]:
            
            stack.pop()
            lis.pop()
        
        return len(stack) == 0