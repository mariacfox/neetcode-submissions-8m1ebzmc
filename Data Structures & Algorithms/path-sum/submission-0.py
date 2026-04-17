# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr_sum):
            if not node: return False

            curr_sum += node.val
            if not node.left and not node.right: # no children
                return curr_sum == targetSum

            return ((dfs(node.left, curr_sum)) or (dfs(node.right, curr_sum)))
            
        return dfs(root, 0) # curr_sum == 0 at start