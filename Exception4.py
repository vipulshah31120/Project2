#NZEC error
#generally multiple inputs are separated by commas and we read them using input() or int(input()),
# but most of the online coding platforms while testing gives input separated by space and in those
# cases int(input()) is not able to read the input properly and shows error like NZEC.
#Intead of using the code below,
#n = int(input())
#k = int(input())
#print n," ",k
# Use:

n, k = input().split(" ")       #when entering values we have to give a space,  used in split()
n = int(n)
k = int(k)

print(n,"",k)
