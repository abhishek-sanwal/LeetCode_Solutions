class Solution:
    def splitArray(self, arr: List[int], K: int) -> int:
        
        N = len(arr)
        mi=max(arr)
    
        ma=sum(arr)
    
        ans=ma # ans is my max possible answer.
        
        while(mi<=ma):
    
            mid=(mi+ma)//2
    
            subarr=0
    
            su=0
    
            for i in range(N):
    
                su+=arr[i]

                if (su>mid):

                    subarr+=1

                    su=arr[i]

            if (subarr+1)<=K:

                ans=mid

                ma=mid-1

            else:

                mi=mid+1
        return ans
    