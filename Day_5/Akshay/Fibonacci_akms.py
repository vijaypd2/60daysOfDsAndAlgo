# Uses python3
import sys
def calc_fib(n):
 if(n<=1 ):
  return n
 else:
  a=[0,1]
  for i in range(2,n+1):   
  		 a.append(a[i-1]+a[i-2])
  return a[n]
n=int(input())
print(calc_fib(n))
