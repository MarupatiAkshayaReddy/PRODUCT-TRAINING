#pre-order:-root-left-right
#in-order:-left-root-right
#post-order:-left-right-root
class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def display(root):
    if root==None:
        return
    #pre-order
    print(root.data)
    display(root.left)
    display(root.right)
    
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
display(root)

print()
print()
q=[]
q.append(root)
while q:
    a=q.pop(0)
    print(a.data,end=" ")
    if a.left:
        q.append(a.left)
    if a.right:
        q.append(a.right)
