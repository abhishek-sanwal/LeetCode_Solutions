class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        A = nums
        K = k
        N = len(A)
        B = [0] * (N + 1)
        for i in range(N): B[i + 1] = B[i] + A[i]
        d = collections.deque()
        res = N + 1
        for i in xrange(N + 1):
            while d and B[i] - B[d[0]] >= K: res = min(res, i - d.popleft())
            while d and B[i] <= B[d[-1]]: d.pop()
            d.append(i)
        return res if res <= N else -1

        