num1=int(input("Enter the first number: "))
operator=raw_input("Choose operator: ")
num2=int(input("Enter the second number: "))
if operator=="+":
    print num1+num2
elif operator=="-":
    print num1-num2
elif operator=="*":
    print num1*num2
elif operator=="/":
    print num1/num2
elif operator=="%":
    print num1%num2
elif operator=="**":
    print num1**num2
else:
    print "Invalid operator."
