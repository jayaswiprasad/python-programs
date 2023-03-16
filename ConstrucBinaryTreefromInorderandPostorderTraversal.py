class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        in_map = {}
        
        for i in range(len(inorder)):
            in_map[inorder[i]] = i
        
        def func(inorder, postorder, start, end, in_map):
            if start >= end:
                if inorder == [] or start > end:
                    return None
                
                if self.pindex >=0:
                    node = postorder[self.pindex]
                    self.pindex -= 1
                    
                return TreeNode(inorder[start])
            else:
                if self.pindex >=0:
                    node = postorder[self.pindex]
                    self.pindex -= 1            
            
            root = TreeNode(node)
            idx = in_map[node]

            root.right = func(inorder,  postorder, idx + 1, end, in_map)
            root.left = func(inorder, postorder,start, idx - 1, in_map)
            
            return root
        
        self.pindex = len(postorder) - 1
        return func(inorder, postorder, 0, len(inorder) - 1, in_map)
