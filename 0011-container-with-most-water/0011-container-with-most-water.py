class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # Area of rectangle
        
        #Area of rectangle = length * breadth
        
        #I will take maximum breadth and reduce it one by one
        
        i = 0
        
        j = len(height) - 1
        #height = [1,8,6,2,5,4,8,3,7] , mini = 8 , curr_area = 8*6 = 48
        
        maxi = 0
        
        while i < j:
            
            mini = min(height[i], height[j])
            
            curr_area = mini * (j-i)
            
            maxi = max(maxi,curr_area)
            
            if mini == height[i]:
                i += 1

            if mini == height[j] :
                
                j -= 1
                
        return maxi
    
    
        maxi = 0
        
        for i in range(len(height)):
            
            for j in range(i+1,len(height)):
                
                mini = min(height[i],height[j])
                
                maxi = max(maxi,mini*(j-i))
                
        return maxi
        