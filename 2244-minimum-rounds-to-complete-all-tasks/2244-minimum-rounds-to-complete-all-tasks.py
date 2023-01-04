class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        hashmap = Counter(tasks)
        print(hashmap)
        count = 0
        
        for i in hashmap:
    
            if hashmap[i] == 1:
                return -1
            
            if hashmap[i] %3==0:
                count += hashmap[i]//3
            else:
                count += hashmap[i]//3 + 1
        
        return count