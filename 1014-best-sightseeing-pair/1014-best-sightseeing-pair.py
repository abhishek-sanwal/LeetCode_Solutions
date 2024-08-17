class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        right = [0]*len(values)
        right[-1] = values[-1] - (len(values)-1)

        for i in range(len(values)-2,-1,-1):

            right[i] = max(right[i+1], values[i]-i)

        maxi = 0

        for i in range(len(values)):
            if i < len(values)-1:
                maxi = max(maxi, values[i]+i + right[i+1])

        return maxi