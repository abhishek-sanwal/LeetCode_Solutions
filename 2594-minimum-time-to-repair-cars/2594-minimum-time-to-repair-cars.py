class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        # [1,2,3,4] cars = 10

        # if x is ans then x+1....infinte all are ans

        # if x not ans then 0....x can not be ans

        low = min(ranks)
        high = 10**18

        def valid(mid):
            
            count = 0
            for rank in ranks:
                count += floor((mid//rank)**0.5)
            return count >= cars

        while low <= high:

            mid = (low + high)//2

            if valid(mid):

                high = mid - 1

            else:
                low = mid + 1

        return low

