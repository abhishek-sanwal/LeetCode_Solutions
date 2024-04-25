class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = list()
        
        s = [i for i in s]
        
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