class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0 for _ in range(len(temperatures))]
        for j, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                e, i = stack[-1]
                stack = stack[:-1]
                answer[i] = j - i
            stack.append((t, j))
        return answer