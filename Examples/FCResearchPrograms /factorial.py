def factorial():
    fact=1
    n=int(input("enter the n: "))
    for i in range(n):
        fact=fact*(i+1)

    print("n!=",fact)
    
factorial()
