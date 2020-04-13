#!/usr/bin/python3

def fibonacci(n):
	if n==1 or n==2:
		return 1
	else:
		return fibonacci(n-1)+fibonacci(n-2)

n=int(input("fibonacci number?"))
for i in range(1,n+1):
	print(fibonacci(i))
print("F",n,"=",fibonacci(n))
