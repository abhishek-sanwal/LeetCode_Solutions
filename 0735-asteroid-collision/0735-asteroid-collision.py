class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = list()

        for ele in asteroids:

            # Going to right directions    
            if ele > 0:

                stack.append(ele)

            # Someone is going to left direction Can cause RL 
            else:
                
                # RL Collions
                while stack and stack[-1] > 0 and stack[-1] < abs(ele):
                    stack.pop()

                # stack top and ele is equal
                if stack and stack[-1] == abs(ele):
                    stack.pop()
                    
                elif not stack or stack[-1] < 0:
                    stack.append(ele)

        return stack