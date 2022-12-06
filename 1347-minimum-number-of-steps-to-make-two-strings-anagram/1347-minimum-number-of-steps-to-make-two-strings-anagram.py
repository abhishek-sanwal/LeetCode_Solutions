class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        count = 0
        hashmap = defaultdict(int)
        for char in s:

            hashmap[char] += 1

        for char in t:

            if char in hashmap:
                
                hashmap[char] -= 1

                if not hashmap[char]:
                    del hashmap[char]

            else:
                count += 1 
    
        return count

