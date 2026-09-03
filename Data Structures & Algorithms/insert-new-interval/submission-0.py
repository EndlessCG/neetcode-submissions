class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        post = 0
        for iv in intervals:
            if iv[0] > newInterval[1]:
                break
            post += 1
        new_start, new_end = newInterval
        pre = post - 1
        while pre > -1:
            if new_start > intervals[pre][1]:
                break
            new_end = max(new_end, intervals[pre][1])
            new_start = min(new_start, intervals[pre][0])
            intervals.pop(pre)
            pre -= 1
        intervals.insert(pre + 1, [new_start, new_end])
        return intervals

        