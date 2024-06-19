class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(mid):
            
            # m groups with k consecutive each
            groups = 1
            sumi = 0
            for i in weights:
                
                sumi += i

                if sumi > mid:
                    groups += 1
                    sumi = i

                

            return groups <= days

        low = max(weights)

        high = sum(weights)

        while low <= high:

            mid = (low +(high-low)//2)

            if valid(mid):

                high = mid - 1

            else:
                low = mid + 1

        return low