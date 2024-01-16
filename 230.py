class Solution:
    def kthSmallest(self, root, k):
        # p=root
        # stack=[]
        # while p or stack:
        #     while p:
        #         stack.append(p)
        #         p=p.left
        #     p=stack.pop()
        #     k-=1
        #     if k==0:
        #         return p.val
        #     p=p.right
        def dfs(root, time, ans):
            if root is None:
                return
            if time[0]>0:
                dfs(root.left, time, ans)
            time[0]-=1
            if time[0]==0:
                ans[0]=root.val
            if time[0]>0:
                dfs(root.right, time, ans)
        ans=[]
        time=[k]
        dfs(root, time, ans)
        return ans[0]