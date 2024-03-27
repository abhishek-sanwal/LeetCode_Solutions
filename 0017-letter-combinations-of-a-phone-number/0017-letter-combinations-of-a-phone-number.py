class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            
            return []
        digit_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        ans = []
        
        def backTrack(idx,curr):
            #print(curr,idx==len(digits))
            # Base Condition
            if idx == len(digits):
                #print(curr,ans)
                ans.append("".join(curr))
                
                return None
            
            # Iteration
            for x in digit_map[digits[idx]]:

                curr.append(x)
                backTrack(idx+1,curr)
                curr.pop()
            #curr.pop()      
            return None
        
        backTrack(0,[])
        return ans
        
                
            