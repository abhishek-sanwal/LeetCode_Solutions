class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        lis = []
        
        check_A = set()
        check_B = set()
        intersection = set()
        count = 0
        for i in range(min(len(A),len(B))):

            check_A.add(A[i])
            check_B.add(B[i])
            if A[i] in check_B:
                
                intersection.add(A[i])
            
            if B[i] in check_A:
                
                intersection.add(B[i])
            
            lis.append(len(intersection))
            
        return lis