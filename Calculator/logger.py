from datetime import datetime as dt


def calculation_logger(a, action, b, result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write(f'{time} {a} {action} {b} = {result}\n')