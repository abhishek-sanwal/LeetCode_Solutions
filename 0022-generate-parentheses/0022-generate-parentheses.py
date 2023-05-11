class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        
        curr = []
        
        def generate(opening,closing):
            
            # Bounded function
            if closing > opening or opening > n or closing > n:
                
                return 
            
            if opening ==n and closing==n:
                
                print(opening,closing,curr)
                ans.append("".join(curr))
            
            curr.append("(")
            generate(opening+1,closing)
            curr[-1] = ")"
            generate(opening,closing+1)
            curr.pop()
            return 
            
        generate(0,0)
        
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        res = []
        
        curr = []
        
        opening = closing = n
        
        def generate(opening , closing ):
            
            if closing < opening or opening == -1 or closing ==-1:

                return 
            
            if opening == 0 and closing == 0:
                
                res.append("".join(curr))
                
                return 
            
            curr.append("(")

            generate(opening - 1 , closing )

            curr[-1] = ")"

            generate(opening , closing - 1 )

            curr.pop()
            
        generate( opening , closing )
        
        return res
        