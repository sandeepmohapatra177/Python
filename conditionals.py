day_of_week =input("Enter the day of the week:").lower() #print the lower
print("day_of_week")

if day_of_week == "sat" or day_of_week =="sun": #=:assign | ==: compare
    print("I will not go to office")
else:
    print("I need to go to office")
    

num1=int (input("enter first number: "))#string input
num2=int (input("enter second number: "))

choice =input("Choose operation: (options: + ,-,*,/,%):")
 
if choice == "+":
    sum_of_num = num1 + num2
    print("addition:", sum_of_num)

elif choice == "-":
    difference_2_nums = num1 - num2
    print("substraction:", difference_2_nums)

elif choice == "*":
    prod_of_num = num1 * num2
    print("multiplication:", prod_of_num)

elif choice == "/":
    divison_2_nums = num1 / num2
    print("division:", divison_2_nums)

elif choice == "%":
    remainder_of_2nos = num1 % num2
    print("remainder:", remainder_of_2nos)

else:
    print("invalid error")
 
 