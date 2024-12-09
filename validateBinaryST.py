class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None

        def inOrder(root):
            nonlocal prev
            
            if not root:
                return True
            
            left_result = bool(inOrder(root.left))

            if (left_result == False): return False

            if(prev and prev.val >= root.val):
                return False
            
            prev = root

            right_result = bool(inOrder(root.right))

            if(right_result == False): return False
            return True
        
        return inOrder(root)

