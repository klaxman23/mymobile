#Write a program to print if user enter any number for that table.


num = int(input("Enter a value:"))

for i in range(1,11):
    print(f"{num} * {i} = {num*i}")
    
