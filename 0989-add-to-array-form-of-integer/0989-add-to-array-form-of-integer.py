class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        nums = arr = num
        
        carry = 0
        
        ans = deque()
        
        for i in range(len(nums)-1,-1,-1):
            
            carry,x = divmod(k%10 + nums[i] + carry,10)
            k//= 10
            ans.appendleft(x)
            
        while k:
            
            carry,x = divmod(k%10 +carry,10)
            k //= 10
            ans.appendleft(x)
            
        if carry:
            ans.appendleft(carry)
            
        return ans
                
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        for i in range(len(nums)-1,-1,-1):
            
            y = 0
            
            if curr > -1:
                
                y = ord(k[curr]) - 48
            
            sumi = (arr[i] + y + carry) % 10
            carry = (arr[i] + y + carry )  // 10
            #print(sumi,carry,i,arr[i])
            arr[i] = sumi
            curr -= 1
            
        if carry:
            
            return [carry] + num
        
        if curr>-1:
            #print(k[:curr+1],num)
            x = [int(i) for i in k[:curr+1]]
            return x + num
        
        return num
            

            
            
            
            