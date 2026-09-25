class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anaset = set()

        for word in strs:
            anaset.add("".join(sorted(word)))

        set_to_index = dict()
        cnt = 0
        for word in anaset:
            set_to_index["".join(sorted(word))] = cnt
            cnt+=1

        res = [[] for _ in range(cnt)]

        for word in strs:
            (res[set_to_index["".join(sorted(word))]]).append(word)

        return res