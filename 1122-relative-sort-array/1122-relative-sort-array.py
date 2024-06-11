class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        freq = [0]*1001
        
        for i in arr1:
            
            freq[i] += 1
            
        index = 0
        
        for i in arr2:
            while freq[i] > 0:
                
                arr1[index] = i
                index += 1
                freq[i] -= 1 
                
        for i in range(1001):
            
            while freq[i] > 0:
                arr1[index] = i
                index += 1
                freq[i] -= 1 
                
        return arr1