class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [i for i in s]
        mapp_closing = {
            
            ")" :"(",
            "}" : "{",
            "]" : "["
        }
        
        var = -1
        
        for i in s:
            
            if i in mapp_closing:
                
                # No matching opening bracket found expression is invalid.
                if var == -1 or s[var] != mapp_closing[i]:
                    #print(var,i,s[var])
                    return False
                
                # Pop the opening bracket
                var -= 1
                
            else:
                var += 1
                s[var] = i
                
        return var == -1
                
                
                