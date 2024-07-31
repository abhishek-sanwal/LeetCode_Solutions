class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        @lru_cache(maxsize=1000)
        def recursion(curr_width,index, answer):
            
            if index == len(books):
                
                return answer
            
            if curr_width - books[index][0] >= 0 :
                
                return min(recursion(curr_width - books[index][0],index + 1, max(answer, books[index][1])), 
                           answer + recursion(shelfWidth - books[index][0], index + 1, books[index][1]) ) 
            
            
            return answer + recursion(shelfWidth - books[index][0], index + 1, books[index][1])
        
        
        return recursion(shelfWidth, 0, 0)