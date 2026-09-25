class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcounts=Counter(t)
        scounts = defaultdict(int)

        resl = resr = -1

        l = 0
        matches = 0
        for r in range(len(s)):
            scounts[s[r]] +=1


            if s[r] in tcounts and scounts[s[r]] == tcounts[s[r]]:
                matches +=1

            while matches == len(tcounts):
                if resl == -1 or r - l < resr - resl:
                    resl, resr = l, r
                
                left_ch = s[l]
                scounts[left_ch] -= 1
                
                if left_ch in tcounts and scounts[left_ch] < tcounts[left_ch]:
                    matches -= 1
                l +=1



        return "" if resl == -1 else s[resl: resr+1]
             
            


