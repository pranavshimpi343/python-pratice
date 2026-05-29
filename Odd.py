# Find Greatest of Two Numbers and Check Even/Odd

a = int(input("Enter the first number :"))
b = int(input("Enter the secound number :"))
 
if a > b :
    print("a is greatest among 2")
    if a % 2 == 0:
        print("a is Even")
    else:
        print("a is Odd")

else:
    print("b is greatest among 2")
    if b % 2 == 0:
        print("b is Even")
    else:
        print("b is Odd")
         