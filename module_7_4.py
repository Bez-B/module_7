# Домашнее задание по теме "Форматирование строк".

team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды %s' % team1
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды {}'.format(team2)
else:
    challenge_result = 'Ничья!'


# Конкатенация
print('Приветствуем' + 'участников' + 'соревнования' + 'и болельщиков!')

# Форматирование с использованием символа «%»
print('В команде %s, участников: %d' % (team1, team1_num))
print('В команде %(name_team)s, участников: %(num_people)d' % {'name_team': team2, 'num_people': team2_num})
print('Итого сегодня в командах участников: %s и %d!' % (team1_num, team2_num))

# Форматирование с использованием метода .format()
print('Команда {} решила задач: {}!'.format(team1, score_1))
print('Команда {1} решила задач: {0}!'.format(score_2, team2))
print('{} решили задачи за {} с!'.format(team1, round(team1_time, 2)))
print('{} решили задачи за {} с!'.format(team2, round(team2_time, 1)))

# Форматирование с использованием f-строк
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по '
      f'{round((team1_time + team2_time) / (score_1 + score_2), 1)} секунды на задачу!')
