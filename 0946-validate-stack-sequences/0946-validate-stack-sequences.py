class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        j = 0
        stack  = []
        for i in pushed:

            stack.append(i)
            
            while stack and stack[-1] == popped[j]:
                
                stack.pop()
                j+=1
        
        return len(stack) == 0
        
            
                