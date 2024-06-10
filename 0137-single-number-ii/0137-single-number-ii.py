class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        bits = [0]*32
        
        sign_bit = 0
        
        for element in nums:
            
            bit = 0
            
            if element < 0:
                sign_bit += 1
                sign_bit %= 3
            
            element = abs(element)
            
            while element:
                
                if element & 1:
                    
                    bits[bit] += 1
                    bits[bit] %= 3
                
                element >>= 1
                bit += 1
        
        ans = 0
        
        for bit in range(0,32):
            
            bits[bit] %= 2
            
            if bits[bit]:
                
                mask = 1 << bit
                ans |= mask
        
        if sign_bit == 0:
            
            return ans
        
        return "This case will never occur" if sign_bit == 2  else -ans
        
        
#         xor_of_array = single_element ^ (xor_of_triple_elements)
        
#         set bits at ith position = 
        
#         odd no of set bits at ith position then  only it will be set
#         even no of set bits then unset
        
#             10
#             10
#             11
#             10
            
#             01
#             10
            
#          #  01 
#         <------- right to left
        
#         3 no of set bits 1
        
        
#         4 no of set bits at 1th = 0
#         1 no of set bits at 0th = 1
#         xor_of_array = 1