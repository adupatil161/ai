def move(a,b):
    print("move",a,"to",b)

def TowerOfHanoi(n,A,B,C):
    if n==1:
        move(A,C)

    else:
        TowerOfHanoi(n-1,A,C,B)
        move(A,C)
        TowerOfHanoi(n-1,B,A,C)
n=(int(input("enter the number of disks:")))
TowerOfHanoi(n,"A","B","C")



#OUTPUT
'''enter the number of disks:3
move A to C
move A to B
move C to B
move A to C
move B to A
move B to C
move A to C'''
