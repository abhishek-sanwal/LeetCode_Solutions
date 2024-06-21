class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        # I can make minutes consecutive ones to zeros 
        
        # [1,0,1,2,1,1,7,5] customers

        # [0,1,0,1,0,1,0,1] grumpy

        # all k length substrings now I need to find corresponding max_customers
        # [0,1,0]
        # [1,0,1]
        # [0,1,0]
        # [1,0,1]
        # [0,1,0]
        # [1,0,1]

        # custome= [1,0,1,2,1,1,7,5]
        # grumpy = [0,1,0,1,0,1,0,1]
        # minutes = 3
        # 0 => cc = 1 max =1 size =1 front =0
        # 1=> cc = 1 max=1 size =2 front = 0 
        # 2=> cc=2 max=2 size =3 front = 0
        # 3 => cc=4-1=3 max =3 size =3 front = 1
        # 4=>cc=4 max=4 size = 3 front=2 
        # 5=> cc=5-1 =4  max = 4 front  = 3
        # 6 => cc = 11-2=9 max = 9 front =4
        # 7 => 
        
        # 0(N) Time and 0(1) space solution

        # 0(N) time 
        # It is asking for overall array not just window of size minutes 
        # Sliding window is calcualting  optimal result for window of size minutes
        suffix = 0
        for i in range(len(customers)):
            suffix += customers[i]*abs(1-grumpy[i])

        # 0(N) Time 
        front = curr_customers = max_customers =  0
        for rear in range(len(customers)):

            # calculate suffix[rear+1]
            # Substract if grumpy[rear] is zero
            suffix -= customers[rear]*abs(1-grumpy[rear])
            curr_customers += customers[rear]

            # Slide window by 1 to make its length minutes
            if (rear - front + 1) > minutes:
                # Substract only if grumpy[front] was 1
                curr_customers -= customers[front] * grumpy[front]
                front += 1
            # Calculate curr_valid_window + suffix[i+1]
            max_customers = max(max_customers, curr_customers + suffix)
        
        return max_customers


            

        