class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        
        if len(s) != len(t):
            return False
            
        arr = [0] * 26
        
        for a,b in zip(s,t):
            
            if a == b:
                continue
            
            count = (ord(b) - ord(a) + 26) % 26
            # print(count,"before")
            if arr[count] > 0:
                
                count += 26 *arr[count]
            # print(count,"after")
            if count > k:
                
                return False
            
            arr[count%26] += 1
        # print(arr)
        return True
        
        
        
        