class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        
        counts = Counter(nums)
        num = min(counts.keys())  # start from minimum number
        
        while k > 0:
            counts[num] -= 1 
            counts[num+1] += 1
            if counts[num] == 0:  # if there are no more elements in this "bucket" or number, then we go to the next highest num
                num += 1
                
            k -= 1
        
        product = 1
        for num, count in counts.items():
            if count > 0:
                product *= (num**count)
            
        return product % (10**9 + 7)
        
        
        heapify(nums)
        
        for i in range(k):
            
            heappush(nums, heappop(nums) + 1)
        
        sol = 1
        mod = 10**9 + 7
            
        for i in nums:
            
            sol = (sol * i) % mod
            
        return sol
    
    