class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        memo = {}
        
        def recursion(curr_width,index, answer):
            
            if index == len(books):
                
                memo[(curr_width, index)] = answer
                return answer
            
            if (curr_width, index) in memo:
                
                return memo[(curr_width, index)]
            
            if curr_width - books[index][0] >= 0 :
                
                memo[(curr_width, index)] = min(recursion(curr_width - books[index][0],index + 1, max(answer, books[index][1])), 
                           answer + recursion(shelfWidth - books[index][0], index + 1, books[index][1]) ) 
                
                return memo[(curr_width, index)]
            
            
            memo[(curr_width, index)] = answer + recursion(shelfWidth - books[index][0], index + 1, books[index][1])
            
            return memo[(curr_width, index)]
        
        
        return recursion(shelfWidth, 0, 0)