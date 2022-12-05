class Solution:
    
    def frequencySort(self, s: str) -> str:
        
        hashmap = defaultdict(int)
        
        for i in s:
            hashmap[i] += 1
            
        arr = sorted(hashmap,key=lambda x: hashmap[x],reverse=True)
        
        temp = list()
        
        for i in arr:
            
            temp.append(i*hashmap[i])
            
        return  "".join(temp)
        
        
        
        
        
        
        
        
        
        
        
        
        
        s = [i for i in s]
        
        arr = [0]*52
        
        for char in s:
            
            if ord(char) < 97:
                
                arr[ord(char)-65] += 1
                
                
            else:
                arr[ord(char)-97] += 1
                
        print(arr)
        
        