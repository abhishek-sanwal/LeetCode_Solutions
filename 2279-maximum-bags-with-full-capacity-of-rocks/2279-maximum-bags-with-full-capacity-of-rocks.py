class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], add: int) -> int:
        
        for i in range(len(capacity)):
            
            capacity[i] -= rocks[i]
            
        tot = 0
        
        capacity.sort()
        
        for i in range(len(capacity)):
            
            if capacity[i] == 0:
                
                tot += 1
                continue
            
            add -= capacity[i]
            
            if add<0:
                break
            tot += 1
            
        return tot
            
        
        
        