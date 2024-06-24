class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s =s2
        p = s1
        k = len(s1)
        count_p = Counter()
        front = 0
        for i in p:

            count_p[i] += 1

        count = Counter()

        for rear in range(len(s2)):

            count[s[rear]] += 1

            if rear-front +1 >k:

                count[s[front]] -= 1
                if not count[s[front]]:
                    del count[s[front]]
                front += 1
            
            if count == count_p and rear-front+1==k:
                
                return True

        return False
