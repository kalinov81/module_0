import numpy as np

count = 0                            # Счетчик попыток
number = np.random.randint(1, 101)   # Загадали число
print ("Загадано число от 1 до 100")


def game_core_v3(number):
    '''
    Функция принимает загаданное число и возвращает число попыток.
    В зависимомсти от того, predict больше или меньше number,
    увеличиваем, либо уменьшаем его на 2.
    Счетчики итераций увеличения и уменьшения сигнализируют нам о том,
    что predict пересек number, после пересечения нужно его откатить на 1.
    Количество попыток при таком подходе сократилось в 2 раза по сравнению
    с v2, результат не оптимальный, но и не было задачи достичь
    минимального количества попыток.
    '''
    count = 1                            # Счетчик кол. попыток
    increases_count = 0                  # Счетчик итераций с увеличением
    decreases_count = 0                  # Счетчик итераций с уменьшением
    predict = np.random.randint(1, 101)  # Предполагаемое число

    while number != predict:
        count += 1
        if number > predict:
            if decreases_count == 0:
                predict += 2
                increases_count += 1
            else:
                predict += 1
        elif number < predict:
            if increases_count == 0:
                predict -= 2
                decreases_count += 1
            else:
                predict -= 1

    return(count)  # Выход из цикла, если угадали


def score_game(game_core):
    # Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    count_ls = []
    np.random.seed(1)  # Фикс. RANDOM SEED, для воспроизводимости эксперимента
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v3)
