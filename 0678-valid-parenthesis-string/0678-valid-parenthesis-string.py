class Solution:
    def checkValidString(self, s: str) -> bool:
        
        open_count = close_count = 0
        
        high = len(s) - 1
        
        for low in range(len(s)):
            
            if s[low] in ["(","*"]:
                
                open_count += 1
                
            # Means we have matched this
            else:
                open_count -= 1
                
            if open_count < 0:
                return False
                
        for i in range(len(s)-1,-1,-1):
            
            if s[i] in [")","*"]:
                
                close_count += 1
                
            else:
                close_count -= 1
            
            if close_count < 0:
                return False
            
        return True
            
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