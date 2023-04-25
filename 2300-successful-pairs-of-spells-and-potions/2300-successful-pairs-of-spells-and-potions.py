
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        ans = []
        portions = potions
        portions.sort()
        
        ans = []
        for i in spells:
            
            # Leftmost value greater than or equal to x
            x = bisect_left(portions,ceil(success/i))
            if x == len(portions):
                
                ans.append(0)
                
            else:
                ans.append(len(portions)-x)
        
        return ans
        