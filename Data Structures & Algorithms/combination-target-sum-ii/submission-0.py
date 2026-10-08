class Solution:
    def combinationSum2(self,  nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        cod = []

        cnt = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev != nums[i]:
                cod.append((prev, cnt))
                cnt = 0
                prev = nums[i]
            cnt += 1
        cod.append((prev, cnt))
        res = []

        def dfs(i, arr):
            if i == len(cod) or sum(arr) >= target:
                if sum(arr) == target: res.append(arr)
                return


            cnt = []
            for _ in range(cod[i][1]):
                cnt.append(cod[i][0])
                dfs(i+1, arr + cnt)

            dfs(i+1, arr)

        dfs(0, [])
        return res
