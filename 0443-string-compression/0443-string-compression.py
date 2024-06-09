class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i = 0
        res = 0
        while i < len(chars):
            group_length = 1
            while (i + group_length < len(chars)
                   and chars[i + group_length] == chars[i]):
                group_length += 1
            chars[res] = chars[i]
            res += 1
            if group_length > 1:
                str_repr = str(group_length)
                chars[res:res+len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += group_length
        return res
        
        j = 0
        
        lis = []

        i = 0
        s = chars
        while i < len(s):

            curr = s[i]
            count = 0
            while i< len(s) and s[i] == curr:

                i += 1
                count += 1
            
            if count != 1:
                j += 1
                for x in str(count):
                    
                    chars[j] = x 
                    j += 1 
            else:
                j += 1
            if i >= len(chars):
                
                return j
            
            
            j = i
                
        return j-1
                
                
            
                
            
                
    