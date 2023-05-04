from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        q1 = deque()
        q2 = deque()
        
        for i in range(len(senate)):
            
            if senate[i]=="D":

                q1.append(i)
            
            else:
                q2.append(i)
                
        while q1 and q2:
            
            idx1,idx2 = q1.popleft(),q2.popleft()
            
            if idx2 > idx1:
                
                q1.append(idx2+len(senate))
                
            else:
                q2.append(idx1+len(senate))
                
        return "Dire" if q1 else "Radiant"