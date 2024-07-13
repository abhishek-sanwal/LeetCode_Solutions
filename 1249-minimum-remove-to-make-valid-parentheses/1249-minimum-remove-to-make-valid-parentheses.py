class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        s = [i for i in s]
        
        high = len(s)-1
        
        open_count = close_count = 0
        
        for i in range(len(s)):
            
            if s[i] == "(":
                
                open_count += 1
                
            elif s[i] == ")":
                open_count -= 1
                
            if s[high-i] == ")":
                
                close_count += 1
                
            elif s[high-i] == "(":
                close_count -= 1
            
            if open_count < 0:
                open_count = 0
                s[i] = ""
                
            if close_count < 0:
                close_count = 0
                s[high-i] = ""
            
        return "".join(s)
        stack = list()
        for i,ele in enumerate(s):
            
            if ele == ")":
                
                if not stack:
                    s[i] = ""
                    continue
                stack.pop()
                
            elif ele == "(":
                stack.append(i)
        
        while stack:
            s[stack.pop()] = ""
        
        return "".join(s)