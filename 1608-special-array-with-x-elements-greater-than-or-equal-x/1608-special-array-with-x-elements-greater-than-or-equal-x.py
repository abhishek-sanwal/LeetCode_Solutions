class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        freq = [0]*1001
        
        for ele in nums:
            
            freq[ele] += 1
            
        for i in range(999,-1,-1):
            
            freq[i]  += freq[i+1]
            if freq[i] == i:
                
                return i 
            
        return -1