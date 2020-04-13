#!/usr/bin/python3

sum=0
n=int(input("number:"))

for i in range(1,n+1):
	a=int(input("input number:"))
	sum+=a

average = sum/n
print(average)
