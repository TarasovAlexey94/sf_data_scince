import numpy as np
import random
random_number = random.randint(1, 101) # Загадывае слуайное число в выбраннном  диапазоне

def game_v3(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        
    Returns:
        int: Число попыток
    """
    count = 0
    min = 1
    max = 100
    while True: # Запускаем цикл отбора
        count += 1
        mid = (min + max)//2 # Приеняем метод деленния на 2
        if mid == random_number:
            break  # выход из цикла, если угадали
        elif mid > random_number:
            max = mid
        else:
            min = mid
    return (count) # Возвращем число попыток

def score_game(game_v3) -> int:
    """За какое количество попыток в среднем из 1000 подходов 
    угадывает наш алгоритм

    Args:
        game_v3 ([type]): функция угадывания


    Returns:
        int: среднее количество попыток
    """
    count_1s = []   # Cписок для сохранения количества попыток
    np.random.seed(1)   # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size = (1000))  # Загадали список чисел
    for number in random_array:
        count_1s.append(game_v3(number))
    score = int(np.mean(count_1s))  # Находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за : {score} попыток')
    return(score)
# Run
score_game(game_v3)