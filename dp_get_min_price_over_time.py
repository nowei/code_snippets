# I accidentally read a question wrong on leetcode, but I came up something
# that solves something else
# costs[0] = 1 day, costs[1] = 3 days, costs[2] = 7 days
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        dp[0] = min(costs)
        for i in range(1, days[-1]):
            dp[i] = min(dp.get(i - 1, 0) + costs[0], dp.get(i - 7, 0) + costs[1], dp.get(i - 30, 0) + costs[2])
        print(dp)
        return 
