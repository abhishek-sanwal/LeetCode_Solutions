class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        cost = 0
        seats.sort()
        students.sort()
        
        for i in range(len(seats)):
            
            cost += abs(seats[i]-students[i])
            
        return cost