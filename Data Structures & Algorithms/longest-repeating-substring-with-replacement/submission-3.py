class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def get_index(char): return ord(char) - ord('A')

        n = len(s)
        chars = [0] * 27
        

        res =0

        l = 0
        for r in range(n):
            chars[get_index(s[r])] +=1

            if r - l + 1 - max(chars) > k:
                chars[get_index(s[l])] -=1
                l+=1

            res = max(res, r - l + 1)

        return res


            


