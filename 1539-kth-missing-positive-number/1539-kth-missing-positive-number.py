class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        

#         [2,3,4,7,11]

#         [1,2,3,4,5,]


        low = 0
    
        high = len(arr)-1
        
        while low <= high:
            
            mid = (low + high) //2
            
            if arr[mid] - (mid+1) >= k:
                
                high = mid -1

            else:
                low = mid + 1
        print(low)
        return low + k
        