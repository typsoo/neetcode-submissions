class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcounts=Counter(t)
        scounts = defaultdict(int)


        
        resl = resr = -1

        matches = 0
        l = 0
        for r in range(len(s)):
            scounts[s[r]] +=1
            matches

            while l <= r and (scounts[s[l]] > tcounts[s[l]] or not s[l] in tcounts):
                scounts[s[l]] -=1
                l +=1

            if r - l + 1 >= len(t):
                flag = True
                for ch in tcounts.keys():
                    if tcounts[ch] > scounts[ch]:
                        flag = False
                        break
                
                if flag:
                    if resl == -1 or r - l < resr - resl:
                        resl, resr = l, r

        return "" if resl == -1 else s[resl: resr+1]
             
            


