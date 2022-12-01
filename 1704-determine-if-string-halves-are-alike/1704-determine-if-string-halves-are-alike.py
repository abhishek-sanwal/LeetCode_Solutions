class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        def count_vowels(start,end,s):
            
            vowels =["A","a","E","e","i","I","O","o","U","u"]
        
            count = 0
            
            for i in range(start,end):
                
                if s[i] in vowels:
                    
                    count += 1
                    
            return count
        
        return len(s)%2==0 and count_vowels(0,len(s)//2,s) == count_vowels(len(s)//2,len(s),s)