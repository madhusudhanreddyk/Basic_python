def encryption():
    print("to calculate encryption value(m^emodn)\nenter m value")
    m = int(input())
    print("enter  e value")
    e = int(input())
    print("enter n value")
    n = int(input())
    b = str(m**e%n)
    print("the encryption value is:"+b)
