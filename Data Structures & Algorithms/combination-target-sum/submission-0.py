class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []

        def dfs(i, arr):
            if i == len(nums) or sum(arr) >= target:
                if sum(arr) == target:
                    res.append(arr)
                return

            dfs(i, arr + [nums[i]])
            dfs(i+1, arr)

        dfs(0, [])
        return res
