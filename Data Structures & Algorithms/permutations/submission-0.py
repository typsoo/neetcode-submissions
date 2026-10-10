class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n

        res = []
        comb = []
        def dfs(i):
            if i == n: 
                res.append(comb.copy())
                return 

            for j in range(n):
                if not used[j]:
                    used[j] = True
                    comb.append(nums[j])
                    dfs(i+1)
                    used[j] = False
                    comb.pop()

        
        dfs(0)
        return res