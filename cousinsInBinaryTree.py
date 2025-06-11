from collections import deque
class TreeNode:
    def __init__ (self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def isCousins(self,root,x,y):
        if not root:
            return False
        
        queue=deque([(root,None)])
        while queue:
            size=len(queue)
            x_parent=y_parent=None

            for _ in range(size):
                node,parent=queue.popleft()

                if node.val==x:
                    x_parent=parent
                elif node.val==y:
                    y_parent=parent

                if node.left:
                    queue.append((node.left,node))
                if node.right:
                    queue.append((node.right,node))
            if x_parent and y_parent:
                return x_parent != y_parent
            if x_parent or y_parent:
                return False
            
        return False
    
def buildTree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue=deque([root])
    i=1
    while queue and i<len(values):
        node=queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left=TreeNode(values[i])
            queue.append(node.left)
        i+=1
        if i<len(values) and values[i] is not None:
            node.right=TreeNode(values[i])
            queue.append(node.right)
        i+=1
    return root

root=buildTree([1,2,3,None,4,None,5])
sol=Solution()
print(sol.isCousins(root,5,4))
        



