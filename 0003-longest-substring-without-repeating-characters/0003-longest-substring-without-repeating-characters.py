class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapp = {}
        
        # Sliding window problem
        
        maxi = front = 0
        
        for rear in range(len(s)):
            
            if s[rear] in mapp:
                
                idx = mapp[s[rear]]
                
                for j in range(front,idx+1):
                    
                    del mapp[s[j]]
                    
                front = idx + 1
            
            mapp[s[rear]] = rear
            
            maxi = max(maxi,len(mapp))
            
        return maxi
            
            