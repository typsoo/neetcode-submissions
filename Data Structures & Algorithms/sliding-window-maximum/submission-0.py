class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        pq = []
        res = []


        for i in range(k):
            heapq.heappush(pq, -nums[i])

        removed = defaultdict(int)
        res.append(-pq[0])



        l = 0
        for r in range(k, n):
            heapq.heappush(pq, -nums[r])
            removed[nums[l]] +=1
            l+=1

            while removed[-pq[0]] > 0:
                removed[-pq[0]] -=1
                heapq.heappop(pq)

            res.append(-pq[0])

        return res