class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        
        count = [0]*26
        maxi = 0
        for i in s:
            
            # count how many elements were less than s-k in 
            x = ord(i) - ord('a')
            c = 1
            for i in range(x,min(26,x+k+1),1):
                c = max(c,count[i]+1)
                
            for i in range(x,max(-1,x-k-1),-1):
                c = max(c,count[i]+1)
            #print(count,c)
            
            count[x] = c
            maxi = max(maxi,c)
        
        return maxi
    
        memo = {}
        arr = s
        def recursion(idx, last_ele, curr_length):
            
            if idx == len(s):
                
                return curr_length
            
            if (idx,last_ele,curr_length) in memo:
                
                return memo[(idx,last_ele,curr_length)]
            
            maxi = curr_length
            
            if abs(ord(last_ele)-65 -(ord(s[idx])-65)) <= k:
                
                # I can take this element
                
                maxi = max(maxi,recursion(idx+1, arr[idx],curr_length+1))
            
            # Start new chain from this element
            maxi = max(maxi,recursion(idx+1,arr[idx],1))
            
            # ignore this element
            maxi = max(maxi,recursion(idx+1,last_ele,curr_length))
            memo[(idx,last_ele,curr_length)] = maxi
            
            return memo[(idx,last_ele,curr_length)] 
        
        return recursion(1,s[0],1)