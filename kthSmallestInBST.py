class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k

        def inOrder(root):
            nonlocal count

            if not root:
                return None
            
            left_result = inOrder(root.left)

            if left_result: return left_result

            count -= 1

            if(count == 0):
                return root.val
            
            right_result = inOrder(root.right)

            if right_result: return right_result
            return None
        
        return inOrder(root)