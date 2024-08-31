#calculator
num1 =int(input("enter num1:"))
num2 =int(input("enter num2:"))

operator = input("enter operator:")

match operator:
    case "+":
        print("sum of number",num1 +num2)
    case "-":
        print("difference of number is:",num1 -num2)
    case "*":
        print("multiplication of number is:",num1 *num2)
    case "/":
        print("divison of number is:",num1 /num2)
    case "_":
        print("enter a valid operator")    
