class Solution:
    def morrisInorderTraversal(self, root):
        res = []
        curr = root

        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                # Find the rightmost node in left subtree
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right

                if not pre.right:
                    # Threading: make a temporary link to curr
                    pre.right = curr
                    curr = curr.left
                else:
                    # Thread exists: remove it and visit curr
                    pre.right = None
                    res.append(curr.val)
                    curr = curr.right

        return res
