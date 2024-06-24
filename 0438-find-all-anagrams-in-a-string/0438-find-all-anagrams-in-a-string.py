class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ans = list()
        k = len(p)
        count_p = Counter()
        front = 0
        for i in p:

            count_p[i] += 1

        count = Counter()

        for rear in range(len(s)):

            count[s[rear]] += 1

            if rear-front +1 >k:

                count[s[front]] -= 1
                if not count[s[front]]:
                    del count[s[front]]
                front += 1
            # print(count,count_p,rear)
            if count == count_p:
                # print(rear)
                ans.append(rear-k+1)

        return ans
