from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def rightSideView(self,root):
        if not root:
            return[]
        
        result=[]
        queue=deque([root])

        while queue:
            level_size=len(queue)
            for i in range(level_size):
                node=queue.popleft()

                if i == level_size-1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
def buildTree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue=deque([root])
    i=1
    while queue and i <len(values):
        node=queue.popleft()
        if i < len(values)and values[i] is not None:
            node.left=TreeNode(values[i])
            queue.append(node.left)
        i +=1
        if i <len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i+=1
    return root
    
root=buildTree([1,2,3,None,5,None,4])
sol=Solution()
print(sol.rightSideView(root))