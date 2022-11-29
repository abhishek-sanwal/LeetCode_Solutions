class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        count_y = customers.count("Y")
        
        left_n = 0
        mini = 10**9
        
        for i in range(len(customers)):

            curr_penality = count_y + left_n
            
            if curr_penality < mini:
                mini = curr_penality
                ans = i
                
            if customers[i] == "N":
                left_n += 1
                
            else:
                count_y -= 1
                
        return i+1 if count_y + left_n < mini else ans
        
            
                
            
            
            
            