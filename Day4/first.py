name = input("Enter your name: ")
""" if len(name)>6:
    print("Hi my name is ",name)
else:
    print(f"Hi my name is invalid name") """

print("Hi my name is ",name if len(name)>6 else 'invalid name')