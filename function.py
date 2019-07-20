
 

def say_hi():
    print("hi")
def say_hello():
    print("hello")
def add_2_number(a=None,b=None):
    if(a is None):
        a=int(input("nhap so a "))
    if(b is None):
        b=int(input("nhap so b "))
    return a+b

def evaluete(so1,so2,pt):
    if pt=='+':
        return so1+so2
    elif pt=='-':
        return so1-so2
    elif pt=='*':
        return so1*so2
    else:
        return so1/so2

import time
import math
def is_prime(n):
    
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3,n,2):
            if(n%i==0):
                return False
    return True
def is_prime_to(v):
    list=[]
    for i in range(2,v,1):
        if(is_prime(i)==True):
            list.append(i)
    print(list)

def Eratosthenes(n):
    list=[i for i in range(0,n+1,1)]
    list[0]=0
    list[1]=0
    for v in range(2,int(math.sqrt(n)),1):
        if list[v]!=0:
            for j in range(v*v,n+1,v):
                list[j]=0
    print(list)


    # for i in range(2,int(math.sqrt(n)),1):
    #     if list[i]!=0:
    #         for v in range(i*i,n,i):
    #             list[v]=0
    # print(list)
# Eratosthenes(100000000000000)


# is_prime_to(100000000000000)


# nếu đặt số a=none thì nhập như nào
# list=[1,2,3,4,5]
# x=0
# for v in list:
#     x+=add_2_number(x,v)