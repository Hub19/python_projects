#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
def game_core(number):
    '''Проверяем в какой половине находится загаданное число и меняем значения области. Функция возвращает число попыток.'''
    count = 1
    left = 1
    right = 101
    np.random.seed(1)
    predict = np.random.randint(left, right)
    if number == predict:
        count = 1
    else:
        while predict != number:
            if number > (left+right) // 2:
                left = (left+right) // 2
                predict = np.random.randint(left, right)
                count += 1
            elif number < (left+right) // 2:
                right = (left+right) // 2
                predict = np.random.randint(left, right)
                count += 1
            elif number == (left+right) // 2:
                predict = (left+right) // 2
                count += 1
    return(count)


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
score_game(game_core)


# In[ ]:




