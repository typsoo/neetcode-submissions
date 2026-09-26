class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        pq = []
        res = []

        for r in range(n):
            heapq.heappush(pq, (-nums[r], r))

            if r >= k - 1:
                while pq[0][1] <= r - k:
                    heapq.heappop(pq)

                res.append(-pq[0][0])

        return res