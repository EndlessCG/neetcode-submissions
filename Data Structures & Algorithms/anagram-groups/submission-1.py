from collections import Counter
def counter_to_str(counter: Counter) -> str:
    return str(sorted(counter.items()))
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        output_ls = []
        for s in strs:
            if counter_to_str(Counter(s)) in seen:
                output_ls[seen[counter_to_str(Counter(s))]].append(s)
            else:
                seen[counter_to_str(Counter(s))] = len(output_ls)
                output_ls.append([s])
        return output_ls