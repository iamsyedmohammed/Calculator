#print("This is a Calculator")
print("Select from the Given Operations")
print("Addition:")
print("Subtraction:")
print("Multiplication:")
print("Division:")
give=input()
if give=="Addition":
    num1=int(input("Enter the first number:\n"))
    num2=int(input("Enter Second Number:\n"))
    sum=int(num1)+int(num2)
    print("THe sum is:\n",sum)

elif give=="Subtraction":
     num1=int(input("Enter first Number:\n"))
     num2=int(input("Enter the second Number:\n"))
     diff=int(num1)-int(num2)
     print("The Difference is:\n",diff)
elif give=="Division":
          num1 = int(input("Enter first Number:\n"))
          num2 = int(input("Enter the second Number:\n"))
          div = float(num1) / float(num2)
          print("The Answer is:\n", div)
elif give == "Multiplication":
    num1 = int(input("Enter first Number:\n"))
    num2 = int(input("Enter the second Number:\n"))
    mul = float(num1) * float(num2)
    print("The Answer is:\n ", mul)
else:
    print("Invalid Entry!")