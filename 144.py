class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val=val 
        self.left=None 
        self.right=None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traversal(root, ans):
            if root is None:
                return 
            ans.append(root.val)
            traversal(root.left, ans)
            traversal(root.right, ans)
            return ans
        return traversal(root, [])


def levelOrderConstruction(values):
    if not values:
        return None
    
    index = 0
    root = TreeNode(values[index])
    index += 1
    
    queue = [root]
    while queue:
        node = queue.pop(0)
        
        if index < len(values):
            if values[index] is not None:
                node.left = TreeNode(values[index])
                queue.append(node.left)
            index += 1
        
        if index < len(values):
            if values[index] is not None:
                node.right = TreeNode(values[index])
                queue.append(node.right)
            index += 1
    
    return root

# 示例输入
node_values =[1,None,2,3]

# 构建二叉树
root_node = levelOrderConstruction(node_values)
print(Solution().preorderTraversal(root_node))

