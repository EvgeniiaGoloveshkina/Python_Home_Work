def get_value():
       
    return float(input('Введите  значение = '))

def get_action():
    action = input('Выберите одну из операций: + - * /  ')
    while action not in ('+-/*'):
        action = input('Такой операции нет. Выберите одну из операций: + - * /  ')
    return action

def show_result(result):
    print(f'Результат = {result}')