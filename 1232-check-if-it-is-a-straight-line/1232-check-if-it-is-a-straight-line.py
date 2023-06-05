class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        (x0, y0), (x1, y1) = coordinates[: 2]
        
        dx ,dy = (x1-x0),(y1-y0)
        
        for x, y in coordinates:
            
            if dx * (y - y1) != (x - x1) * dy:
                return False
        return True