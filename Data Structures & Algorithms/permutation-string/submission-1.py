class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = defaultdict(int)
        for c in s1:
            s1dict[c]+=1

        s2dict = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            if s2[r] not in s1dict:
                l = r + 1
                s2dict.clear()
            else:
                s2dict[s2[r]] +=1

                while l <=r and s2dict[s2[r]] > s1dict[s2[r]]:
                    s2dict[s2[l]] -=1
                    l +=1
                
                if r - l + 1 == len(s1): return True

        return False
