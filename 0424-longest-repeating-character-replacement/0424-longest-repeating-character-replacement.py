class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        mapp = defaultdict(int)
        maxi = ans = front = 0
        
        # Sliding window
        for rear in range(len(s)):
            
            # Updating in hashamp
            mapp[s[rear]] += 1
            
            # calculating maximum frequency
            maxi = max(maxi, mapp[s[rear]])
            
            other_char_freq = (rear - front + 1) - maxi
            #print(rear-front+1,mapp,maxi,other_char_freq)
            # If there are more than k other chars shift the window
            if other_char_freq > k:
                print("true")
                # 0(k)
                while  (rear-front +1) - max(mapp.values()) >k:
                    
                    mapp[s[front]] -=1
                    front += 1
                
            ans = max(ans,rear-front+1)
            
        return ans
            
        
        
#         Suppose I have a window in which I can consider atmost k different characters a
        
#         rear-f
        
#         k=2
#          |aabb|ccc
            
#         mapp ={
#             a:1
#             b:2  k>= len(window) -maxi_frequncey 0(k) update at each index
#         } maxi = 2
        
#         front slide window