class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):
            
            return False
        
        arr = []
        
        unmatch = 0
        
        for i in range(len(s)):
            
            if unmatch >2:
                break
            
            if s[i] != goal[i]:
                arr.append([i,s[i]])
                unmatch += 1
                
        if unmatch not in [0,2]:
            return False
        
        if unmatch == 0:
            
            return True if any(s.count(x) > 1 for x in string.ascii_lowercase) else False
            
        return True if arr[0][1]== goal[arr[1][0]] and goal[arr[0][0]] == arr[1][1] else False
                