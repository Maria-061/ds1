"""Игра угадай число.
Компьютер сам загадывает и угадывает число за минимальное количество попыток
"""
import numpy as np

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
#            print(f"Вы угадали число! Это число = {number}, за {count} попыток")
            break # конец игры, выход из цикла
                   
    return(count)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток

    random_array = np.random.randint(1, 101, size=(10000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

score_game(random_predict)