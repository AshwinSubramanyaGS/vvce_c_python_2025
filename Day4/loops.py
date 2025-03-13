#Creating variable to take user input
multiple=int(input("Enter a no"))

#loop to print the tables
for multiplier in range(1,11):
    print(f"{multiple} X {multiplier} = {multiple*multiplier}")