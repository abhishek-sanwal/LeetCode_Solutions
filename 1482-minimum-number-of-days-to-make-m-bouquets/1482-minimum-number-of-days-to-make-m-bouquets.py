class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1

        def valid(mid):
            
            # m groups with k consecutive each
            groups = consecutive = 0
            for i in bloomDay:

                if i <= mid:
                    consecutive += 1

                else:
                    consecutive = 0

                if consecutive == k:

                    groups += 1
                    consecutive = 0
                    
            return groups >= m

        low = 0

        high = max(bloomDay)

        while low <= high:

            mid = (low +(high-low)//2)

            if valid(mid):

                high = mid - 1

            else:
                low = mid + 1

        return low