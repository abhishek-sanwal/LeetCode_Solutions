class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        check = Counter()

        front = maxi = sumi =  0
        # [1,5,4,2,9,9,9] k = 3
        # {1,5,4} sumi = 10 size = 3
        # {5,4,2} sumi = 11 size = 3
        # {4,2,9} sumi = 15 size = 3
        # {9,9}
        for rear in range(len(nums)):

            check[nums[rear]] += 1
            sumi += nums[rear]
        
            while rear-front+1 >k or rear-front + 1 > len(check):
                
                check[nums[front]] -= 1
                if not check[nums[front]]:
                    del check[nums[front]]
                    
                sumi -= nums[front]
                front += 1

            if rear-front +1 == k:
                maxi = max(maxi,sumi)

        return maxi


