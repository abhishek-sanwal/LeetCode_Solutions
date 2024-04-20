class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        mapp_closing = {
            
            ")" :"(",
            "}" : "{",
            "]" : "["
        }
        
        stack = []
        
        for i in s:
            
            if i in mapp_closing:
                
                # No matching opening bracket found expression is invalid.
                if not stack or stack[-1] != mapp_closing[i]:
                    
                    return False
                
                # Pop the opening bracket
                stack.pop()
                
            else:
                stack.append(i)
                
        return len(stack) == 0
                
                
                