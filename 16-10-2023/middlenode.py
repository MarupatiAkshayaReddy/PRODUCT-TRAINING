'''class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
o1=node(1)
o1.next=node(2)
o1.next.next=node(3)

print(o1.val,o1.next.val,o1.next.next.val)'''

'''class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None

def insertatbeg(head,data):
    pass
    
l=[2,4,6,8,9]
head=node(l[0])'''


class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
   
    
    def insertatlast(self,val):
        if self.head==None:
            self.head=node(val)
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            new=node(val)
            curr.next=new
            #curr.next=node(val)
    
    
    def middleNode(self):
        slow=self.head
        fast=self.head
       
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
           
        return slow.val
                    
    def printing(self):
        temp=self.head
        while(temp):
            print(temp.val,end="->")
            temp=temp.next
    

l=[2,4,6,8,9,10]
o=sll()
for i in l:
    o.insertatlast(i)
o.printing()

print()
print(o.middleNode())




