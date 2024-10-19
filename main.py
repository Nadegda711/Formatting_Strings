team1_num = 5
team2_num = 6
print("В команде Мастера кода участников: %s !" % team1_num)
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))


score_2 = 42
team1_time = 18015.2
team2_time = float()
result1 = "Команда Волшебники данных решила задач: {} !".format(score_2)
result2 = "Волшебники данных решили задачи за {} с !".format(team1_time)
print(result1)
print(result2)


score_1 = 40
print(f"Команды решили {score_1} и {score_2} задач.")
challenge_result1 = "победа команды Мастера кода!"
challenge_result2 = 'Победа команды Волшебники Данных!'
print(f"Результат битвы: {challenge_result1}")
tasks_total = 82
time_avg = 350.4
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")




if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = challenge_result1
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = challenge_result2
else:
    print('Ничья!')