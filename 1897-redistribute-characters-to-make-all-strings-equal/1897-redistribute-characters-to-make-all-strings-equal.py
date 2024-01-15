class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return all(c % len(words) == 0 for c in Counter(chain(*words)).values())
        x = Counter()
        
        for i in words:
            
            x+=Counter(i)
            
        return all(not x[i]%len(words) for i in x)