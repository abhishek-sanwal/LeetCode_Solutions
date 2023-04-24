
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        ans = []
        portions = potions
        portions.sort()
        
        for i in spells:
            
            x = bisect_left(portions,ceil(success/i))
            #print(x,portions,len(portions)-x)
            if x == len(portions):
                
                ans.append(0)
                
            else:
                ans.append(len(portions)-x)
        
        return ans
        