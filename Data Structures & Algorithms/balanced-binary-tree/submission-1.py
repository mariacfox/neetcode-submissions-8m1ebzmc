# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs returns a pair: [is_balanced_subtree, height_of_subtree]
        def dfs(node: Optional[TreeNode]) -> List[int]:
            if not node:
                # Base case: an empty subtree is balanced and has height 0
                return [True, 0]

            # Recurse on left and right children to gather their status
            left_balanced, left_height  = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            # A node's subtree is balanced if:
            # 1) left subtree is balanced
            # 2) right subtree is balanced
            # 3) heights differ by at most 1
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

            # Height of current subtree: 1 + max(height of left, height of right)
            height = 1 + max(left_height, right_height)

            return [balanced, height]

        return dfs(root)[0]  # We only need to know if the whole tree is balanced
        