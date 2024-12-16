class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # LNR NLR
        # time- O(n2) space - O(n2)
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        inorderIndex = 0

        for i in range(len(inorder)):
            if inorder[i] == root.val:
                inorderIndex = i
        
        leftPreorderSubtree = preorder[1:inorderIndex+1]
        rightPreorderSubtree = preorder[inorderIndex+1:len(preorder)]

        leftInorderSubtree = inorder[0:inorderIndex]
        rightInorderSubtree = inorder[inorderIndex+1:len(inorder)]

        root.left = self.buildTree(leftPreorderSubtree, leftInorderSubtree)
        root.right = self.buildTree(rightPreorderSubtree, rightInorderSubtree)
            
        return root
    
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = dict()
        p = 0
        if (len(preorder) == 1): 
            return TreeNode(preorder[0])
        
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i

        def helper(start, end):
            nonlocal p

            if (start > end) or (p == len(inorder)):
                return None
            
            inorderIndex = hashmap.get(preorder[p])
            root = TreeNode(preorder[p])

            p += 1

            root.left = helper(start, inorderIndex-1)
            root.right = helper(inorderIndex+1, end)

            return root
        return helper(0,len(inorder)-1)
        

        
    