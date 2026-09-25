class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        l, r = 0, n-1

        while l <= r:
            mid = (r + l) // 2

            if nums[-1] < nums[mid]:
                l = mid + 1
            else:
                if mid == 0 or nums[mid-1] > nums[mid]: return nums[mid]
                r = mid - 1

        return nums[l]
