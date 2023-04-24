class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def fun(s):
            
            s = [i for i in s]
            
            prev = -1
            
            for i in range(len(s)):
                
                if s[i] == "#":
                    
                    prev = prev if prev < 0 else prev-1
                    
                else:
                    prev+=1
                    s[prev] , s[i] = s[i] ,s[prev]
                    
            print(s,s[:prev+1] if prev>-1 else "")
            return "".join(s[:prev+1]) if prev>-1 else ""
        
        return fun(s) == fun(t)
                    
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        stack = list()
        
        for i in s:
            
            if i=="#":
                
                if stack:
                    stack.pop()
            
            else:
                
                stack.append(i)
                
                
        s = "".join(stack)
        stack = []
        for i in t:
            
            if i=="#":
                if stack:
                    stack.pop()
            
            else:
                
                stack.append(i)
        return "".join(stack) == s
        