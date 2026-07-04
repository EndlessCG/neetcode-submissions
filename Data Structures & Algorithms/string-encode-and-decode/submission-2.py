class Solution:

    def encode(self, strs: List[str]) -> str:
        lens = [len(s) for s in strs]
        lens_strs = ["0" * (3 - len(str(l))) + str(l) for l in lens]
        len_lens_strs = "0" * (3 - len(str(len(lens_strs)))) + str(len(lens_strs))
        return "".join(strs) + "".join(lens_strs) + len_lens_strs

    def decode(self, s: str) -> List[str]:
        len_lens_strs = int(s[-3:])
        lens_strs = [int(s[i:i+3]) for i in range(-3-3*len_lens_strs, -3, 3)]
        strs = []
        i = 0
        for l in lens_strs:
            strs.append(s[i:i+l])
            i += l
        return strs