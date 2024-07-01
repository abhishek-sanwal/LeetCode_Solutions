class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        row = len(image)
        
        col = len(image[0])
        
        def isValid(i,j):
            
            return i>-1 and i< row and j>-1 and j<col
        
        directions = [
            [1,0],[0,1],[-1,0],[0,-1]
        ]
        count = 0
        def bfs(x,y,org):
            
            que = deque([[x,y]])
            nonlocal count
            while que:
                # if count ==10:
                #     return
                for _ in range(len(que)):
                    
                    x,y = que.popleft()
                    
                    for x1,y1 in directions:

                        new_x, new_y = x+x1,y+y1

                        if isValid(new_x, new_y) and image[new_x][new_y] == org:
                          
                            image[new_x][new_y] = color
                            que.append([new_x, new_y])
                    
            return None
        
        if image[sr][sc] == color:
            return image
        
        org = image[sr][sc]
        image[sr][sc] = color
        bfs(sr,sc,org)
        return image