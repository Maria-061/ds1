"""Игра угадай число.
Компьютер сам загадывает и угадывает число за минимальное количество попыток
"""
import numpy as np

number = np.random.randint(1, 101) # комьютер загадывает число
count=0 # счетчик

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    x = 1
    y = 101

    while True:
        count += 1
        predict_number = np.random.randint(x, y+1) # предполагаемое число
        
        if predict_number > number:
            y = predict_number

        elif predict_number < number:
            x = predict_number

        else:
            print(f"Вы угадали число! Это число = {number}, за {count} попыток")
            break # конец игры, выход из цикла
            
            
    return(count)

random_predict(number) # Вызов функции