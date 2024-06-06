class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
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
        
        
        
        
        
        
        
        
        
        
        # Without binary search         
        for i in range(1,len(hand)):
            
            match = False
            
            for index in range(len(previous)):
                
                previous_element, curr_size = previous[index]
                
                if curr_size < groupSize and previous_element + 1 == hand[i]:
                    
                    previous[index] = [hand[i],curr_size + 1]
                    match = True
                    break
            
            if not match:
                
                previous.append([hand[i],1])
            # print(previous,required_size)
            if len(previous) > required_size:
                
                return False
            
        return True
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Withour rearrange and maintaing increasing sequence solution
        
#         [1,2,3,6,2,3,4,7,8]
        
        
#         [1,2,3],[6,7,8] ,[2,3,4]
        
        
#         [1,2,3,4,5]
        
#         [1,2,3,4] ,[5]
        
        
        # IF we can not partition array into equal pieces of groupSize then 
        # return False
        if len(hand) % groupSize or not hand:
            
            return False
        
        [1,   2,3,6,2,3,4,7,8]
        
        # We need a list to store previous elements
        # of each group
        previous =  [[hand[0],1]]
        required_size = len(hand)//groupSize 
        
#         [1,2.........n]
        
#         1 scan 1 time
#         2 scan worst case it need
        
#         nth element it need to (n-1) element
        
        # Iterate over array
        for i in range(1,len(hand)):
            
            element = hand[i]
            
            # Replace with first element less than curr_element
            for index in range(len(previous)):
                
                previous_element, curr_size = previous[index]
                
                # Replace operation
                if curr_size < required_size and element > previous_element:
                    
                    previous[index] = [element,curr_size + 1]
                    
            # Check valid or not
            if len(previous) > len(hand) // groupSize:
                
                return False
            
        return True
                
           
        
        
        