class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
        
class cll:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def insertatbeg(self,val):
        if self.head==None:
            self.head=node(val)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            new=node(val)
            new.next=self.head
            self.head.prev=new
            self.head=new
            self.tail.next=self.head
            self.head.prev=self.tail
            
    def deleteatbeg(self):
        if self.head==None:
            return
        
        self.head=self.head.next
        self.tail.next=self.head
        self.head.prev=self.tail
    
    def insertatlast(self,val):
        if self.head==None and self.tail==None:
            self.head=node(val)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            new=node(val)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
            self.tail.next=self.head
            self.head.prev=self.tail
            
    def deleteatend(self):
        if self.head==None:
            return
        self.tail=self.tail.prev
        self.tail.next=self.head
        self.head.prev=self.tail
            
    def printing(self):
        #print(self.head.val,self.head.prev.val,self.tail.val,self.tail.next.val)#to check cyclic is there or not
        print(self.head.val,end="->")
        temp=self.head.next
        while(temp!=self.head):
            print(temp.val,end="->")
            temp=temp.next
    
        


l=[2,4,6,8,9]
o=cll()

'''for i in l:
    o.insertatbeg(i)
o.printing()
print()'''

for i in l:
    o.insertatlast(i)
o.printing()
print()

o.deleteatbeg()
o.printing()
print()

o.deleteatend()
o.printing()
        
