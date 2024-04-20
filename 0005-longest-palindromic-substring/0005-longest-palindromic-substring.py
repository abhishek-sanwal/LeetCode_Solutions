class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        "babad"
        
        #even length = (i-1)
        
        maxi = 0
        
        for i in range(len(s)):
            
            # Odd length
            j = k = i
            while j>-1 and k< len(s) and s[j] == s[k]:
                if maxi < k-j+1:
                    maxi = k-j+1
                    start = j
                j -= 1
                k += 1
            
            
            # Even length
            k = i
            j = i-1
            
            while j>-1 and k<len(s) and s[j] == s[k]:
                if maxi < k-j+1:
                    maxi = k-j+1
                    start = j
                j-=1
                k+=1
        print(start)
        return s[start:start+maxi]
                