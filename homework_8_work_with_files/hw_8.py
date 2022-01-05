while True:
    firstValue = int(input("Enter the first number:"))
    math_operator = input("Choose '+, '-', '/', '*' ")
    secondValue = int(input("Enter the second number:"))

    action_1 = firstValue + secondValue
    action_2 = firstValue - secondValue
    action_3 = firstValue / secondValue
    action_4 = firstValue * secondValue

    if math_operator == '+':
        print(action_1)
        with open('result.txt', 'a') as file:
            file.write(f"\n{firstValue} {math_operator} {secondValue} = {action_1}")

    elif math_operator == '-':
        print(action_2)
        with open('result.txt', 'a') as file:
            file.write(f"\n{firstValue} {math_operator} {secondValue} = {action_2}")

    elif math_operator == '/':
        print(action_3)
        with open('result.txt', 'a') as file:
            file.write(f"\n{firstValue} {math_operator} {secondValue} = {action_3}")

    elif math_operator == '*':
        print(action_4)
        with open('result.txt', 'a') as file:
            file.write(f"\n{firstValue} {math_operator} {secondValue} = {action_4}")

    else:
        print("Error! Maybe you typed smth wrong! \n Check your choice.")


