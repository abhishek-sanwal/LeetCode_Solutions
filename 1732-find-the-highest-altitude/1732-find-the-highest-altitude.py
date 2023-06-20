class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        prev = maxi =  0
        
        for i in range(len(gain)):
            
            prev += gain[i]
            
            maxi = max(maxi,prev)
        
        return maxi
        