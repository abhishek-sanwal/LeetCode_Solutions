class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        arr = nums1 + nums2
        arr.sort()
        
        if len(arr)%2==0:
            
            print(arr[len(arr)//2],arr[(len(arr)//2) -1])
            return (arr[len(arr)//2] + arr[(len(arr)//2) -1] )/2
        
        return float(arr[floor(len(arr)/2)])