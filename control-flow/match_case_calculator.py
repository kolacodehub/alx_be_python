num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second  number: '))
operation = input('Choose the operation (+, -, *, /): ')

match operation:
    case '+':
        if operation == '+':
            result = num1 + num2
            print(result)
    case '-':
        if operation == '-':
            result = num1 - num2
            print(result)
    case '*':
        if operation == '*':
            result = num1 * num2
            print(result)
    case '/':
        if num1 == 0 or num2 == 0:
            print('A 0 cant be used')
        else:
            result = num2 / num1
            print(result)