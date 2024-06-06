class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        hand = nums
        groupSize = k
        
        if not hand or len(hand) %  groupSize:
            
            return False
        
        hand.sort()
        
        required_size = len(hand) // groupSize
        
        previous = [[hand[0],1]]
        
        for i in range(1,len(hand)):
            
            curr_element = hand[i]
            
            # find leftmost element less than curr_element by bs
            
            pos = bisect_left(previous,[curr_element,1])
            
            # Create operation
            if pos == 0 or previous[pos-1][0] != curr_element - 1 or previous[pos-1][1] ==groupSize:
                
                previous.append([curr_element,1])
                
            # Repalce operation
            else:
                previous[pos-1] = [curr_element, previous[pos-1][1] + 1]
                
            # print(previous,pos-1)
            if len(previous) > len(hand) // groupSize:
                
                return False
            
        return True
        
        