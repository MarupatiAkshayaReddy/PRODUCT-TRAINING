class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
        
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def insertatlast(self,val):
        if self.head==None and self.tail==None:
            self.head=node(val)
            self.tail=self.head
        else:
            new=node(val)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
            
    def reverse(self):
        curr=self.head
        while(curr):
            curr.prev,curr.next=curr.next,curr.prev
            curr=curr.prev
        self.head,self.tail=self.tail,self.head
    
    
    def printing(self):
        temp=self.head
        while(temp):
            print(temp.val,end="->")
            temp=temp.next
            
            
l=[2,4,6,8,9]
o=dll()

for i in l:
    o.insertatlast(i)
o.printing()
print()

o.reverse()
o.printing()
print()
