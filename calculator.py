operator = input("Enter an operator (+ - * /) :")
num1 = float(input("Input 1st number : "))
num2 = float(input("Input 2nd number : "))

if operator == "+" :
    result = num1 + num2 
    print(result)
elif operator == "-" :
    result = num1 - num2
    print(result)
elif operator == "*" :
    result = num1 * num2
    print(result)
elif operator == "/" :
    result = num1 / num2
    print(round(result, 2))
else :
    print(f"{operator} is not an valid operator ")
    
