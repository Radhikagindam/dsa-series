class node:
    def __init__(self,data):
        self.val=data
        self.next=None  
def createlinkedlist(arr):
    head=None
    for data in arr:
        if(head==None):
            head=node(data)
            temp=head
        else:
            temp.next=node(data)
            temp=temp.next
    #printlinkedlist(head,arr)
    getdelete(head)
    printlinkedlist(head)
def getdelete(head):
    if(head.next==None):
        return None
    slow=head
    fast=head
    while(fast and fast.next):
        prev=slow
        slow=slow.next
        fast=fast.next.next
    prev.next=slow.next
    slow.next=None
    return head
def printlinkedlist(head):
        temp=head
        while(temp):
            print(temp.val,end="")
            temp=temp.next
          
            print("->",end="")
arr=list(map(int,input().split()))
createlinkedlist(arr)