'''class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
o1=node(1)
o2=node(2)
o3=node(3)

print(o1,o2,o3,sep='\n')
print(o1.val,o2.val,o3.val,sep='\n')

print(o1,o1.val,o1.next)
print(o2,o2.val,o2.next)
print(o3,o3.val,o3.next)'''

#linking the nodes
#o1.next,o2.next,o3.next itself is complete object
class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
o1=node(1)
o2=node(2)
o3=node(3)
o1.next=o2
o2.next=o3

print(o1,o1.val,o1.next)
print(o2,o2.val,o2.next)
print(o3,o3.val,o3.next)
