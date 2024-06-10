class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xor = reduce(lambda x,y:x^y,nums)
        
        xor_group1 = xor_group2 = 0
        
        last_set_bit = xor & -xor
        #rint(last_set_bit)
        for element in nums:
            
            if element & last_set_bit:
                
                xor_group1 ^= element
                
            else:
                
                xor_group2 ^= element
                
        return [xor_group1,xor_group2]
        
        
        bits = [0]*32
        # if bit is 1 it is unset in 1
        # and set in other
        # if bit is 0 gurranteed set in both
        # or unset in both

        # 001  => 1
        # 100  => 4

        # 110

        # 001    010
        # 001    011
        # 101    010

        # #        001
        # #        010
        # #        001
        # #        011
        # #        010
        #          101 

        # 000 => 0
        # 110 => 6

        # 111 => 7
        # 001 => 1

        # #        001
        # #        010
        # #        001
        # #        011
        # #        010
        #          101  

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
            
            if bits[bit]:
                
                mask = 1 << bit
                ans |= mask
        
        if sign_bit == 0:
            
            return ans
        
        return "This case will never occur" if sign_bit == 2  else -ans
        