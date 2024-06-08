class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        hashmap = defaultdict(int)
        
        prefix =  count  = 0
        
        for i in nums:
            
            prefix = (prefix + i) % k
        
            if not prefix:
                count +=1
                
            count += hashmap[prefix]
            
            hashmap[prefix] += 1
            
        return count