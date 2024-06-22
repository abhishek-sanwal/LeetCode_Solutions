class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        ans = 0
        
        front = sumi = pref =  0
        prefix = [0]*len(cardPoints)
        suffix = [0]*len(cardPoints)
        
        for rear in range(len(cardPoints)):
            
            pref += cardPoints[rear]
            prefix[rear] = pref
            
        suffix[0] = prefix[-1]
        
        for i in range(1,len(cardPoints)):
             
            suffix[i] = suffix[i-1] - cardPoints[i-1]
        
        for i in range(k-1):
            
            x = i
            y = k- i -1
            ans = max(ans,prefix[x] + suffix[-y])
            
        return max(ans,prefix[k-1],suffix[-k])
            
#         maximum_sum of k-length subarray
        
#         cardPoints = [1,2,3,4,5,6,1] k = 3
        
#         index  = [0,1,2,3, 4, 5, 6]
#         prefix = [1,3,6,10,15,21,22]
#         suffix = [22,20,17,13,8,2,1]
        

        