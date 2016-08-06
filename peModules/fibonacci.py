from __future__ import print_function, division

fibo = [1,1]
last_index=len(fibo)

def fib(n):
    global fibo,last_index
    if (n>0):
        if(n>last_index):
            for i in range(last_index+1,n+1):
                fibo.append(fibo[i-2]+fibo[i-3])
            last_index=len(fibo)
        return fibo[n-1]
    else:
        print ("Error in index")
        return -1
