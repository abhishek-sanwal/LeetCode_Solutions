class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = list()
        
        ans = ""
        
        for i in s:

            if i != "]" :
                stack.append(i)
                
            else:
                # print(stack)
                char = []
                while stack and stack[-1] != "[":
                    char.append(stack.pop())
                char.reverse()
                char = "".join(char)
                
                stack.pop()
                freq = pow = 0
                while stack and stack[-1].isdigit():
                    
                    freq += int(stack[-1])*10**pow
                    pow += 1
                    stack.pop()
                
                stack.append(char*freq)
        
        return "".join(stack)
                