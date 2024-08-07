class Solution:
    def canPartitionKSubsets(self,nums, k):
    
        S = sum(nums)
        
        # If total sum is not equally divisible by k, then return False
        if S % k != 0:
            return False
        
        partition_sum = S // k
        N = len(nums)
        
        # Memoization cache
        memo = {}
        
        # Sort the numbers in reverse order. It is much easier to 
        # adjust larger elements first. Helps achieve the answer much more quickly.
        nums.sort(reverse=True)
        
        # The recursive search function
        def search(sum_, rem_partitions, visited):
            
            # If the number of partitions remaining is 1, then we've achieved our goal. Return True
            if rem_partitions == 1:
                return True
            
            # If the current sum = partition sum, start a new partition
            # For a new partition, reset current sum to 0 and decrement number of 
            # remaining partitions
            
            if sum_ == partition_sum:
                return search(0, rem_partitions - 1, visited)
            
            # If we've already seen this mask, then return the result
            
            if visited in memo:
                return memo[visited]
            
            # Default answer for the current state.
            ans = False
            
            for i in range(N):
                
                # If the bit at index "i" is unset, that implies it doesn't belong to any partition.
                if visited & (1 << i) == 0 and nums[i] + sum_ <= partition_sum:
                    
                    # If adding it to the current partition returns True, then break. 
                    # No need to recurse further
                    if search(sum_ + nums[i], rem_partitions, visited ^ (1<<i)):
                        ans = True
                        break
            memo[visited] = ans            
            return ans  
        return search(0, k, 0)