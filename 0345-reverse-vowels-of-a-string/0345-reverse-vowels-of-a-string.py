class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s = [i for i in s]
        
        vowels =["a","e","i","o","u","A","E","I","O","U"]
        
        start = 0
        
        end = len(s) - 1
        
        while start < end:
            #print(start,end)
            if s[start] in vowels and s[end] in vowels:
                
                s[start] , s[end] = s[end] , s[start]
                print(start,end)
                start += 1
                end -= 1
                
            elif s[start] not in vowels:
                
                start += 1
                
            else:
                
                end -= 1
            #print(s)
        return "".join(s)
            