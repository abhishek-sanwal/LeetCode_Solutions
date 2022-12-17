class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def eva(x,y,token):
            
            x,y =  int(x),int(y)
            
            if token == "+":
                    
                return x + y

            if token == "-":

                return x-y

            if token == "*":

                return x*y

            return int(x/y) #x//y is not same as int(x/y) for negative numbers
        
        
        stack = []
        
        operator = ["+","-","*","/"]
        
        for token in tokens:
            
            if token in operator:
                
                y = stack.pop()
                x = stack.pop()
                
                stack.append(eva(x,y,token))
                    
            else:
                stack.append(token)
            
            #print(stack)
                
        return int(stack[-1])