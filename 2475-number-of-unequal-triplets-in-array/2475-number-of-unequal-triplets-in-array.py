
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        
        hashmap = dict()
        
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
                
            else:
                hashmap[i] = 1
        
        left = 0
        right = len(nums)
        
        ans = 0
        
        for ele in hashmap:
            
            right -= hashmap[ele]
            ans += left*hashmap[ele] *right
            left +=hashmap[ele]
        return ans
            
        
        check = set(nums)
        count = 0
        for i in range(len(nums)):
            
            for j in range(i+1,len(nums)):
                
                for k in range(j+1,len(nums)):
                    
                    if nums[i]!=nums[j] and nums[j]!=nums[k] and nums[i]!=nums[k]:
                    
                        count+=1
        
        
        return count
        
        
        