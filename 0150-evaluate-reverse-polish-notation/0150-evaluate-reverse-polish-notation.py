class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def evaluate(x,y,token):
            
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
                
                # Remember if expression is 3 4 / then x=3 y=4
                # Changing x and y will impact division and substraction results.
                y = stack.pop() 
                x = stack.pop()
                
                stack.append(evaluate(x,y,token))
                    
            else:
                stack.append(token)
            
            #print(stack)
                
        return int(stack[-1])