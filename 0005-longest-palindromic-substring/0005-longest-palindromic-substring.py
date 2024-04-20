class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        maxi = start = 0
        
        def update(j,k):
            
            nonlocal maxi, start
            while j>-1 and k< len(s) and s[j] == s[k]:
                if maxi < k-j+1:
                    maxi = k-j+1
                    start = j
                j -= 1
                k += 1
            
        for i in range(len(s)):
            
            #odd length
            update(i,i)
            #even length
            update(i-1,i)
            
        return s[start:start+maxi]
                