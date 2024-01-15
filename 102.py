class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        q=[root]
        child=[]
        ans=[]
        while q:
            cur_val=[]
            while q:
                ele=q.pop(0)
                cur_val.append(ele.val)
                if ele.left:
                    child.append(ele.left)
                if ele.right:
                    child.append(ele.right)
            q=child
            child=[]
            ans.append(cur_val)
        return ans
        