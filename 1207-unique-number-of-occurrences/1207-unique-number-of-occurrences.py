class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        return sum(set(collections.Counter(arr).values())) == len(arr)
        
            
        
            
        