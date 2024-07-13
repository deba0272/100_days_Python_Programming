#!/Users/debajyotiroy/anaconda3/bin/python3
import random as rn
computer=rn.choice([-1,0,1])#to generate random number
string=input("enter your choice:")
#here dictionary is used to map the string to the integer(map)
dict1={"s":1,"w":0,"g":-1}
rev_dict={1:"snake",0:"water",-1:"gun"}
user=dict1[string]
print(f"user's choice is:{rev_dict[user]}\ncomputer choice is:{rev_dict[computer]}")
if (user==computer):
    print("Match is draw")
else:
    if(user==1 and computer==0):
        print("uers lose")
    elif(user==0 and computer==1):
        print("user win")
    elif(user==0 and computer==-1):
        print("user lose")
    elif(user==-1 and computer==0):
        print("user win")
    elif(user==-1 and computer==1):
        print("user lose")
    elif(user==1 and computer==-1):
        print("user win")
    else:
        print("invalid input")
print("Finished!!!!!")
