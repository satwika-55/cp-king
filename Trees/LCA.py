
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        def helper(node):
            if not node:
                return None
            left = helper(node.left)
            right = helper(node.right)
            if node == p or node == q:
                return node
            if left and right:
                return node
            return left if left else right
        return helper(root)
