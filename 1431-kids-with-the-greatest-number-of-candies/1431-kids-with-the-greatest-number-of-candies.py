class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        ans = []
        
        m = max(candies)
        
        return [(i + extraCandies >= m) for i in candies]
    
        for i in candies:
            
            ans.append(i + extraCandies >= m)
            
        return ans