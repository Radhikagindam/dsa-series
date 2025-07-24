#to print array ti linked list,linked list contain n number of nodes and for every node it contain random no. of address
class node:
    def __init__(self,data): 
        self.prev=None
        self.val=data  #data
        self.next=None  #add
def createdoublylinkedlist(arr):
    head=None
    for data in arr:
        if(head==None):
            head=node(data)
            temp=head
        else:
            newnode=node(data)
            temp.next=head
            head.prev=temp
            temp=temp.next
    printdoublylinkedlist(arr,head)
def printdoublylinkedlist(arr,head):
    temp=head
    while(temp):
          print(temp.val,end="")  
          temp=temp.next
          
          print("->",end="")
arr=list(map(int,input().split()))
createdoublylinkedlist(arr)