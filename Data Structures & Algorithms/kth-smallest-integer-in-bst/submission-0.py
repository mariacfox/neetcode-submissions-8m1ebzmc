class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative DFS/stack approach
        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right # loop goes back up 