class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, arr):
            if i == len(nums): 
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1, arr)
            subset.pop()
            dfs(i+1, arr + [nums[i]])

        dfs(0, [])
        return res


