class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def buildTree(preorder, inorder):

    def arrayToTree(left,right):

        if left > right:
            return None
        rootvalue=preorder[0]
        root=TreeNode(rootvalue)
        preorder.pop(0)

        root.left=arrayToTree(left,inordermap[rootvalue]-1)
        root.right=arrayToTree(inordermap[rootvalue]+1,right)

        return root



    inordermap={}
    for count,value in enumerate(inorder):
        inordermap[value]=count

    return arrayToTree(0,len(preorder)-1)


        



preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
buildTree(preorder, inorder)