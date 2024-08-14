class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        low = 0
        high = nums[-1] - nums[0]
        
        def valid(mid):

            pairs = front  = 0

            for rear in range(len(nums)):
                
                while nums[rear] - nums[front] > mid:

                    front += 1

                pairs += (rear-front)

            return pairs 

        while low <= high:
            
            mid = (low + high)//2
            
            if valid(mid) < k:
                
                low = mid + 1

            else:

                high = mid - 1

        return low

        temp = []

        for i in range(len(nums)):

            for j in range(i+1,len(nums)):

                heappush(temp,-abs(nums[i]-nums[j]))
                # temp.append(abs(nums[i]-nums[j])
                if len(temp) > k:
                    heappop(temp)

        # temp.sort()
        return -1*temp[0]
        return temp[k-1]
