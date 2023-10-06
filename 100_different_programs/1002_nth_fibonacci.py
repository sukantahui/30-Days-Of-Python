def fibo(num):
    if num in [0,1]:
        return num
    return fibo(num-1)+fibo(num-2)

print(fibo(8))