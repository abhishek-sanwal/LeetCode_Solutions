class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        
        #nums = [-4,-1,-1,0,1,2]
        
        ans = []
        
        for i in range(len(nums)-2):
            
            if nums[i] > 0:
                break
            
            #print(i>0 and nums[i] == nums[i-1])
            # Skip the duplicates
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            # nums[i] + nums[j] + nums[k] = 0
            # nums[j] + nums[k] = -nums[i]
            
            # Two pointer for finding pair with given sum
            j = i + 1
            k = len(nums)-1
            
            while j<k:
                #print(nums[i],nums[j],nums[k])
                if nums[j] + nums[k] > -nums[i]:
                    
                    k -= 1
                    
                elif nums[j] + nums[k] < -nums[i]:
                    
                    j += 1
                    
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                    
        return ans
                
                    
            