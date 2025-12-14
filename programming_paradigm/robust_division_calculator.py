def safe_divide(numerator, denominator):
    try:
        try:
            num = float(numerator)
            den = float(denominator)
        except ValueError:
            print('Error: Please enter numeric values only.')
        else:
            result = num / den
            return f'The result of the division is {result}'
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')