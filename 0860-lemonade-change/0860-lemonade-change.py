class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        count = Counter()
        
        for bill in bills:
            
            original = bill
            bill -= 5
            dollar_20 = (bill // 20)
            bill %= 20
            
            dollar_10 = (bill // 10)
            bill %= 10
            
            dollar_5 = (bill // 5)
            bill %= 5
            
            if not count[20] and dollar_20 > 0:
                
                dollar_10 += 2*dollar_20
                dollar_20 = 0
                
            if not count[10] and dollar_10 > 0:
                
                dollar_5 += 2*dollar_10
                dollar_10 = 0
            
            if (dollar_20 > count[20]) or (dollar_10 > count[10]) or (dollar_5 > count[5]) or bill > 0:
                print(dollar_20,dollar_10, dollar_5, original, count)
                return False
            
            count[20] -= dollar_20
            count[10] -= dollar_10
            count[5] -= dollar_5
            
            count[original] += 1
            
            
        return True