def lemenode(bills:list[int]):
    five=0
    ten=0
    for i in bills:
        if(i==5):
            five+=1
        elif(i==10):
            if(five>0):
                five-=1
                ten+=1
            else:
                return False
        elif(i==20):
            if(five>0 and ten>0):
                five-=1
                ten-=1
            elif(five>=3):
                five-=3
            else:
                return False
        return True

           