class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def kthsmallest(nums1,nums2):
            
            k = floor((len(nums1) + len(nums2))/2) + 1
            #print(k)
            ptr1 = ptr2 = prev = curr = 0
            
            while k and ptr1 < len(nums1) and ptr2< len(nums2) :
                
                prev = curr
                
                if nums1[ptr1] < nums2[ptr2]:
                    
                    curr = nums1[ptr1]
                    ptr1 += 1
                    
                else:
                    
                    curr = nums2[ptr2]
                    ptr2 += 1
                    
                k -= 1
            #print(curr,prev)
            while k and ptr1 < len(nums1):
                prev = curr
                curr = nums1[ptr1]
                ptr1+=1
                k -= 1
            #print(curr,prev)
            while k and ptr2 < len(nums2):
                prev = curr
                curr = nums2[ptr2]
                ptr2 += 1
                k -= 1
                
            #print(curr,prev)
            if (len(nums1) + len(nums2)) % 2 == 1:
                
                return float(curr)
            
            return (prev + curr)/ 2
            
            
        
        return kthsmallest(nums1,nums2)
        
        
        
        
        
        
        
        arr = nums1 + nums2
        arr.sort()
        
        if len(arr)%2==0:
            
            #print(arr[len(arr)//2],arr[(len(arr)//2) -1])
            return (arr[len(arr)//2] + arr[(len(arr)//2) -1] )/2
        
        return float(arr[floor(len(arr)/2)])