class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        count = Counter(s)
        
        ans = list()
        
        for i in order:
            
            ans += i*count[i]
            count[i] = 0
            
        for i in count:
            ans += i*count[i]
            
        return "".join(ans)
        
        