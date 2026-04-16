# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Prepare the result container; each element will be a list of values at one level
        res = []
        # Initialize a queue to hold nodes in BFS order
        q = collections.deque()
        # If the root exists, start BFS from the root
        q.append(root)

        # Process nodes level by level until there are no more nodes to visit
        while q:
            # Number of nodes at the current level (size of the queue for this level)
            q_len = len(q)
            # Collect values for the current level
            level = []

            # Iterate exactly over the nodes at this level
            for i in range(q_len):
                # Dequeue the next node to process
                node = q.popleft()
                # If the node is valid (non-None), record its value and enqueue its children
                if node:
                    level.append(node.val)
                    # Enqueue left child for the next level (if it exists)
                    q.append(node.left)
                    # Enqueue right child for the next level (if it exists)
                    q.append(node.right)
            # If this level has any node values, append it to the result
            if level:
                res.append(level)

        # Return the complete level-order traversal
        return res