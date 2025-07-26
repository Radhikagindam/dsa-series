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
    deletehead(head)
    printlinkedlist(head)
def deletehead(head):
    temp=head.next
    head.next=None
    return temp
def printlinkedlist(head):
    temp=head
    while(temp):
          print(temp.val,end="")
          temp=temp.next
          print("->",end="")
arr=list(map(int,input().split()))
createlinkedlist(arr)