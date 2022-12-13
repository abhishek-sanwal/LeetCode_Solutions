class Solution:
    def splitArray(self, arr: List[int], K: int) -> int:
        
        def valid(mid,arr,K):
            
            subarr=0
    
            su=0
    
            for i in range(len(arr)):
    
                su+=arr[i]

                if (su>mid):

                    subarr+=1

                    su=arr[i]

            if (subarr+1)<=K:
                
                return True
            
            return False
        
        
        
        N = len(arr)
        mi=max(arr)
    
        ma=sum(arr)
    
        ans=ma # ans is my max possible answer.
        
        while(mi<=ma):
    
            mid=(mi+ma)//2
    
            if valid(mid,arr,K):
                ans=mid
                ma=mid-1

            else:

                mi=mid+1
        return ans
    