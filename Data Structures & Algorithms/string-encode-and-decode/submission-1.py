class Solution:


    def encode(self, strs: List[str]) -> str:
        s = ""
        for i, st in enumerate(strs):
            s += f"{len(st)}#{st}"

        return s
            

    def decode(self, s: str) -> List[str]:
        cnt = 0
        res = []
        
        n = len(s)
        i = 0
        while i < n:
            str_number = ""
            while s[i] != '#':
                str_number += s[i]
                i+=1

            number = int(str_number)
            i+=1
            res.append(s[i: i + number])
            i+= number

        return res
