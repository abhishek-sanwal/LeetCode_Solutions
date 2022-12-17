class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def eval(x,y,token):
            x,y =  int(x),int(y)
            if token == "+":
                    
                return x + y

            elif token == "-":

                return x-y

            elif token == "*":

                return x*y

            else:
                return int(x/y)
        
        
        stack = []
        
        operator = ["+","-","*","/"]
        
        for token in tokens:
            
            if token in operator:
                
                y = stack.pop()
                x = stack.pop()
                
                stack.append(eval(x,y,token))
                    
            else:
                stack.append(token)
            
            #print(stack)
                
        return int(stack[-1])