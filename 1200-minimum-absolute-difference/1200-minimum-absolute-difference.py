class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        
        mini = 10**18
        
        lis = list()
        
        for i in range(len(arr)-1):
            
            if arr[i+1] - arr[i] < mini:
                
                mini = arr[i+1] - arr[i]
                lis = [[arr[i], arr[i+1]]]
                
            elif arr[i+1] - arr[i] == mini:
                
                lis.append([arr[i], arr[i+1]])
                
        return lis
                
                