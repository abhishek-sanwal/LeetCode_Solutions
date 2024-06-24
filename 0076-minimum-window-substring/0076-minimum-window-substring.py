class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        count = Counter(t)
        
        mini = len(s) + 1 # impossible
        
        front = 0
        ans = ""
        count_s = Counter()
        
        def similar(x,y):
            
            return all(x[i]>=y[i] for i in y)
        
        for rear in range(len(s)):
            
            count_s[s[rear]] += 1
            # print(rear,count_s,count,similar(count_s,count))
            if similar(count_s,count):

                while similar(count_s,count):
                    
                    count_s[s[front]] -= 1
                    if not count_s[s[front]]:
                        del count_s[s[front]]
                        
                    front += 1

                count_s[s[front-1]] += 1
                front -= 1 
                
            if similar(count_s,count):
                
                if mini > rear-front+1:
                    
                    mini = rear-front+1
                    ans = s[front:rear+1]
                    
        return ans