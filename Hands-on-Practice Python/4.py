# fibonacci series

def main(n):
    if (n < 1):
        return
    a = 0
    b = 1
    print(0,end=" ")
    for i in range(n-1):
        print(b,end=" ")
        c = a+b
        a = b
        b = c


main(eval(input("Enter number : ")))
