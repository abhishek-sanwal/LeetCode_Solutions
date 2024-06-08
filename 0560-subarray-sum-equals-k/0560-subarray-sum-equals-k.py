class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
#         [1,1,1]
        
#         mapp = {} 2
#         prefix_sum = 1
#         mapp ={1:1}
#         prefix_sum = 2
#         mapp ={1:1,2:1}
#         prefix_sum = 3
#         mapp ={1:1,2:2,3:1}
        
#         -----------------_>b
#         --------->a
#                    -------> b-a
        
#         [2:4]  k = 8
#         [1,1,0,0,0,8] prefix_sum = 10
#         [1,2,2,2,2,10]
        
#            .
#         [1,2,3] k =3
#         mapp = {1},prefix_sum = 1
#         mapp = {1:1} ,Prefix_sum = 3
#         mapp = {1:1,3:1;}       ,prefix_sum = 6
        prefix_sum = 0
        
        mapp = {}
        ans = 0
        for index,element in enumerate(nums):
            
            prefix_sum += element
            if prefix_sum == k:
                ans +=1
            if prefix_sum - k in mapp:
                ans += mapp[prefix_sum - k]
                
            mapp[prefix_sum] = mapp.get(prefix_sum, 0 ) + 1
            
        return ans
        