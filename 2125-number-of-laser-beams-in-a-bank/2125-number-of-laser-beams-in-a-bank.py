class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        if len(bank) <2:
            
            return 0
        
        count = curr = 0
        
        for i in bank:
            
            ones = i.count("1")
            
            if ones:
                count += curr*ones
                curr = ones
        
        return count
            
            