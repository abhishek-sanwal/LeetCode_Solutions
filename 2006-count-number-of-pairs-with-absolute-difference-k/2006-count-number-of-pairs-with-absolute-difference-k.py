[1,2,2,1]

[1,2,2.1]

class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        pairs = 0
        
        mapp = {}
        
        for i in range(len(nums)):
            
            if nums[i] + k in mapp:
                
                pairs += mapp[nums[i]+k]
                
            if nums[i]- k in mapp:
                
                pairs += mapp[nums[i]-k]
                
            mapp[nums[i]] = mapp.get(nums[i],0) + 1
            
        return pairs
        
        x = Counter(nums)
        
        pairs = 0
        
        for i in x:
            
            if i-k in x:
                
                pairs +=  x[i-k]
                
            if i+k in x:

                pairs += x[i+k]
                
        return pairs
                
        