class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # Take the tranpose of matrix
        
        row = len(matrix)
        
        col = len(matrix[0])
        
        for i in range(row):
            
            for j in range(i+1,col):
                
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        #print(matrix)
        # Swap miror values
        
        for i in range(row):
            
            matrix[i].reverse()
        return matrix