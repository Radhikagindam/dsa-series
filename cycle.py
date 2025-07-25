#to print array ti linked list,linked list contain n number of nodes and for every node it contain random no. of address
class node:
    def __init__(self,data): #constructor to create a node
        self.val=data  #data
        self.next=None  #add
def createlinkedlist(arr):
    head=None
    for data in arr:
        if(head==None):
            head=node(data)
            temp=head
        else:
            temp.next=node(data)
            temp=temp.next
    print(checkcycle(head))
def checkcycle(head):
    slow=head
    high=head
    while (fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            return True
           
    return False
arr=list(map(int,input().split()))
createlinkedlist(arr)












