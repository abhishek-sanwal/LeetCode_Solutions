class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        front = max_freq = max_length = 0
        
        counter = Counter()
        
        for rear in range(len(nums)):
            
            counter[nums[rear]] += 1
            
            while counter[nums[rear]] > k:
                counter[nums[front]] -= 1
                front += 1

            max_length = max(max_length, rear - front + 1)
            
        return max_length
            