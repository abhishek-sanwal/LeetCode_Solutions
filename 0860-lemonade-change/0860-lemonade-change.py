class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        count = Counter()
        
        currency = [20,10,5]
        
        take = 5
        
        for bill in bills:
            
            original = bill
            bill -= take
            req = 0
            for note in currency:
                
                req += bill // note
                bill %= note
                # print(req,count[note])
                if req <= count[note]:
                    
                    count[note] -= req
                    req = 0
                    
                req *= 2
                
            count[original] += 1
            # print(req,count, original)
            if req>0:
                
                return False
            
        return True