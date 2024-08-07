class Solution:
    def numberToWords(self, num: int) -> str:
        
        def recursion(n):
            
            if n == 0:
                return []
            
            if n <= 20:
                return [starting[n]]
            
            if n <= 99:
                return [tenth[int(n/10)]] + recursion(n-int(n/10)*10)
            
            base_index = int(int(math.log10(n))/3)
            
            base_symbol, base = symbols[base_index]
            
            return recursion(int(n/base)) + [base_symbol] + recursion(n-int(n/base)*base)
        
        starting = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen', 'Twenty']
        
        tenth = ['_', '_', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        
        symbols = [['Hundred', pow(10, 2)], ['Thousand', pow(10,3)], ['Million', pow(10,6)], ['Billion', pow(10,9)]]
        
        words = recursion(num)
        words = " ".join(words)
        return words if words else 'Zero'