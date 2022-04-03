# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root:
            child = dummy = TreeLinkNode(0)
            while root:
                child.next = root.left
                child = child.next or child
                child.next = root.right
                child = child.next or child
                root = root.next
            root = dummy.next