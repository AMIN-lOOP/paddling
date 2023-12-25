addition = lambda numbers: sum(numbers)

subtraction = lambda numbers: numbers[0] - sum(numbers[1:]) if len(numbers) >= 2 else numbers[0]

multiplication = lambda numbers: eval('*'.join(map(str, numbers)))

division = lambda numbers, d: list(map(lambda x: x / d if d != 0 else 'Error - division by zero', numbers))


def get_number(prompt, error_prompt="Please enter a valid number."):
    input_number = input(prompt)
    while not input_number.isdigit():
        print(error_prompt)
        input_number = input(prompt)
    return int(input_number)

numbers_list = []
numbers_list.append(get_number('Enter your first number: '))
numbers_list.append(get_number('Enter your second number: '))

while True:
    need_more = input('Do you need to write more numbers? (yes/no) ').lower()
    if need_more == 'no':
        break
    elif need_more == 'yes':
        numbers_list.append(get_number('Enter your number: '))

operator_options = {'+': addition, '-': subtraction, '*': multiplication, '/': division}

operator_prompt = 'Which operator do you want? (* / + -): '

operator = input(operator_prompt)

while operator not in operator_options:
    print('The option you entered is not valid. Please enter one of the following operators: *, /, +, -')
    operator = input(operator_prompt)

if operator == '/':
    divisor = get_number('What number do you want to divide the numbers by? ')
    for number in numbers_list:
        result = division([number], divisor)
        print(f'result of {number} / {divisor} = {result[0]}')
else:
    result = operator_options[operator](numbers_list)
  
    print(f"The result of the operation is: {result}")
