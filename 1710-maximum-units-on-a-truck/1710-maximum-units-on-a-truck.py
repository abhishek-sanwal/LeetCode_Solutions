class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key=lambda x:(x[1]),reverse=True)
        print(boxTypes)
        profit = 0 
        
        for box in boxTypes:
            
            x = min(truckSize,box[0])
            
            profit += (box[1]*x)
            truckSize -= x
            if truckSize <0:
                break
            print(profit,truckSize,x)
        return profit
    
        
        #50 , 10,28,27
        
        #50 ,5,21  = 81
        