'''145. Binary Tree Postorder Traversal'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = root
        pre = node
        stack = []
        res = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            if node.right is pre or not node.right:
                pre = stack.pop()
                res.append(pre.val)
                node = None
            else:
                node = node.right
        return res