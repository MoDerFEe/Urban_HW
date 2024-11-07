from random import randint as rnd

team1_num = rnd(4, 6)
team2_num = rnd(4, 6)
print('В команде Мастера кода участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
score_1 = rnd(0, 50)
score_2 = rnd(0, 50)
print('Команда Волшебники данных решила задач: {0}!'.format(score_2))
team1_time = rnd(600, 900) / 10 * score_1
team2_time = rnd(600, 900) / 10 * score_2
print('Волшебники данных решили задачи за {0} с!'.format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(f'Результат битвы: {result}')
tasks_total = score_1 + score_2
time_avg=(team1_time/score_1+team2_time/score_2)/2
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
