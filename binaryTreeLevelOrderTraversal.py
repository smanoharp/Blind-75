class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dfs(root, level):
            if not root:
                return root
            
            if(len(result) == level):
                result.append([])
            
            result[level].append(root.val)

            dfs(root.left, level+1)
            dfs(root.right, level+1)
        
        dfs(root, 0)
        return result