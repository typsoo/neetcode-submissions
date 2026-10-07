class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        dp = [False] * n


        def dfs(i, arr):
            if i == len(nums): 
                res.append(arr)
                return
            

            dfs(i+1, arr)
            dfs(i+1, arr + [nums[i]])

        dfs(0, [])
        return res


