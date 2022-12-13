class Solution:
    
    def solve(self,m, n, arr1, arr2):

        arr1ptr = m - 1

        arr2ptr = n - 1

        arrptr = len(arr1) - 1

        while arr2ptr > -1:

            if arr1ptr > -1 and arr1[arr1ptr] > arr2[arr2ptr]:

                arr1[arrptr] = arr1[arr1ptr]
                arr1ptr -= 1

            else:

                arr1[arrptr] = arr2[arr2ptr]
                arr2ptr -= 1

            arrptr -= 1


    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        self.solve(m,n,nums1,nums2)
        