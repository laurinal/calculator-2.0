# checkpoint
#  Define the 4 maths basic function

def add(x,y):
    return x + y
def substract(x,y):
    check = int(input(f"Press 1: {x} - {y}\n Press 2: {y} - {x}\n Response: "))
    if check == 1:
        return x - y 
    elif check == 2:
        return y - x 
    else:
        print("Invalid choice")
    return x - y 
def multiply(x,y):
    return x * y
def divide (x,y):
    check = int(input(f"Press 1:{x} / {y}\n Press 2: {y} / {x} Response:"))
    if check == 1:
        return x/y
    elif check == 2:
        return y/x
    else:
        print("Invalid choice")
    
  
#  putting function in a list
operations = {"add(+)":"", "substract(-)":"", "multiply(*)":"" ,"divide(/)":""}
num = 1
# Create a function 'calculator' that prompts the user to input the first number.
question = str(input("would you like to perform an operation? (Yes or No): ")).capitalize().strip()
while question == "Yes":
    choice = int(input("Press 1 for Addition\nPress 2 to Substract\nPress 3 to Multiply\nPress 4 to Divide\nPress 0 to Quit\nResponse:"))
    if choice == 0:
        break
    elif choice == 1:     
        num1 = float(input("input number: ")) 
        num2 = float(input("input number: ")) 
        add = add(num1,num2) 
        num = num + 1
        print(add)
        question2 = str(input("would you like to continue with your answer? (yes or no):")).lower().strip()
        while question2 == "yes":
            choice = int(input("Press 1 for Addition\nPress 2 to Substract\nPress 3 to Multiply\nPress 4 to Divide\nPress 0 to Quit\nResponse:"))
            if choice == 0:
                break
            elif choice == 1:     
                num1 = add 
                num2 = float(input("input number: ")) 
                add = add(num1,num2) 
                num = num + 1
                print(add)
            if choice == 2: 
                num1 = substract 
                num2 = float(input("input number: ")) 
                sub = substract(num1,num2) 
                num = num + 1
                print(sub)
            elif choice == 3:
                num1 = multiply
                num2= float(input("input number: "))
                multiply = multiply(num1,num2) 
                num = num + 1 
                print(multiply)
            elif choice == 4:
                num1= divide
                num2 = float(input("input number: "))
                divide = divide(num1,num2)
                num = num + 1
                print(divide)
            else:
                print("invalid input")
            
     
    if choice == 2: 
        num1 = float(input("input number: ")) 
        num2 = float(input("input number: ")) 
        sub = substract(num1,num2) 
        num = num + 1
        print(sub)
        question2 = str(input("would you like to continue with your answer? (yes or no):")).lower().strip()
        while question2 == "yes":
            choice = int(input("Press 1 for Addition\nPress 2 to Substract\nPress 3 to Multiply\nPress 4 to Divide\nPress 0 to Quit\nResponse:"))
            if choice == 0:
                break
            elif choice == 1:     
                num1 = add 
                num2 = float(input("input number: ")) 
                add = add(num1,num2) 
                num = num + 1
                print(add)
            if choice == 2: 
                num1 = substract 
                num2 = float(input("input number: ")) 
                sub = substract(num1,num2) 
                num = num + 1
                print(sub)
            elif choice == 3:
                num1 = multiply
                num2= float(input("input number: "))
                multiply = multiply(num1,num2) 
                num = num + 1 
                print(multiply)
            elif choice == 4:
                num1= divide
                num2 = float(input("input number: "))
                divide = divide(num1,num2)
                num = num + 1
                print(divide)
            else:
                print("invalid input")
            
     
    elif choice == 3:
        num1 = float(input("input number: ")) 
        num2= float(input("input number: "))
        multiply = multiply(num1,num2) 
        num = num + 1 
        print(multiply)
        question2 = str(input("would you like to continue with your answer? (yes or no):")).lower().strip()
        while question2 == "yes":
            choice = int(input("Press 1 for Addition\nPress 2 to Substract\nPress 3 to Multiply\nPress 4 to Divide\nPress 0 to Quit\nResponse:"))
            if choice == 0:
                break
            elif choice == 1:     
                num1 = add 
                num2 = float(input("input number: ")) 
                add = add(num1,num2) 
                num = num + 1
                print(add)
            if choice == 2: 
                num1 = substract 
                num2 = float(input("input number: ")) 
                sub = substract(num1,num2) 
                num = num + 1
                print(sub)
            elif choice == 3:
                num1 = multiply
                num2= float(input("input number: "))
                multiply = multiply(num1,num2) 
                num = num + 1 
                print(multiply)
            elif choice == 4:
                num1= divide
                num2 = float(input("input number: "))
                divide = divide(num1,num2)
                num = num + 1
                print(divide)
            else:
                print("invalid input")
            
     
    elif choice == 4:
        num1= float(input("input number: ")) 
        num2 = float(input("input number: "))
        divide = divide(num1,num2)
        num = num + 1
        print(divide)
        question2 = str(input("would you like to continue with your answer? (yes or no):")).lower().strip()
        while question2 == "yes":
            choice = int(input("Press 1 for Addition\nPress 2 to Substract\nPress 3 to Multiply\nPress 4 to Divide\nPress 0 to Quit\nResponse:"))
            if choice == 0:
                break
            elif choice == 1:     
                num1 = add 
                num2 = float(input("input number: ")) 
                add = add(num1,num2) 
                num = num + 1
                print(add)
            if choice == 2: 
                num1 = substract 
                num2 = float(input("input number: ")) 
                sub = substract(num1,num2) 
                num = num + 1
                print(sub)
            elif choice == 3:
                num1 = multiply
                num2= float(input("input number: "))
                multiply = multiply(num1,num2) 
                num = num + 1 
                print(multiply)
            elif choice == 4:
                num1= divide
                num2 = float(input("input number: "))
                divide = divide(num1,num2)
                num = num + 1
                print(divide)
            else:
                print("invalid input")
            
     
    else:
        print("invalid input")
        
    
         
         