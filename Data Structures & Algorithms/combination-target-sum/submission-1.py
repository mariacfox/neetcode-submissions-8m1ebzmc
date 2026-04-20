class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []  # list to store all valid combinations

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())  # if we hit the target, save a copy of the current combination
                return
            if i >= len(nums) or total > target:
                return  # if we've considered all numbers or our sum already exceeded target, stop here

            curr.append(nums[i])       # choose nums[i] and add it to the current combination
            dfs(i, curr, total + nums[i])  # explore further allowing the same number again (unlimited usage)
            curr.pop()                   # backtrack: remove the last added number to try other options
            dfs(i + 1, curr, total)      # move to the next number (skip using nums[i] from now on)

        dfs(0, [], 0)  # start the DFS with index 0, an empty current combination, and total 0
        return res     # return all collected valid combinations