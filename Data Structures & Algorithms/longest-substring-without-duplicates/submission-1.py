class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = defaultdict(int)

        l = 0
        res = 0
        for r in range(len(s)): 
            while chars[s[r]] == 1:
                chars[s[l]] -=1
                l +=1




            chars[s[r]] += 1

            res = max(res, r - l + 1)

        return res