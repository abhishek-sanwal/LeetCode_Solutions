class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapp = dict()
        front = maxi = 0
        for i,ele in enumerate(s):
            
            if ele in mapp:
                
                front = max(front,mapp[ele]+1)
            
            maxi = max(maxi,i-front+1)
            
            mapp[ele] = i
            
        return maxi
