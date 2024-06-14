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
        mod = pow(10,9) + 7
        for num, count in counts.items():
            if count > 0:
                product = (product * pow(num,count,mod)) % mod
            
        return product 
        
        # [2,3,3,6] k = 2
        
        # []
        
        heapify(nums)
        
        for i in range(k):
            
            heappush(nums, heappop(nums) + 1)
            
        mod = pow(10,9) + 7
        
        return reduce(lambda x,y:(x*y) % mod, nums)
        
        sol = 1
        mod = 10**9 + 7
            
        for i in nums:
            
            sol = (sol * i) % mod
            
        return sol
    
    