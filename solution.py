# Вариант 1

# Сгенерировать при помощи escape-символов в консоли изображение флага Франции

RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
SPACE = '         '

for i in range(8):
    print(f'{BLUE}{SPACE}{WHITE}{SPACE}{RED}{SPACE}{END}')


# Сгенерировать в консоли повторяющийся узор (столбец "Узор").

for i in range(3):
    print(f"""
  {WHITE}  {END} 
{WHITE}  {END}  {WHITE}  {END}
  {WHITE}  {END} """)
    

# Сгенерировать в консоли график функции y=x^2 (1 четверти) при помощи escape-символов, минимум 9 строк в высоту (столбец "Функция").

plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i ** 2

step = round(abs(result[0] - result[9]) / 9, 2)

for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8-i) + step

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!!'
    print(line)
print('0\t1 2 3 4 5 6 7 8 9')

# Используя прилагаемый файл с числовой последовательностью ```sequence.txt```, вывести диаграмму процентного соотношения количество чисел меньше и больше 0 

counter_a = 0
counter_b = 0
with open('sequence.txt', 'r') as file:
    list = [float(number) for number in file]
    for number in list:
        if number < 0:
            counter_a += 1
        elif number > 0:
            counter_b += 1
    diagram_height = 25
    start_a = diagram_height - round(counter_a / len(list) * diagram_height)
    start_b = diagram_height - round(counter_b / len(list) * diagram_height)
    WHITEBOX = f'{WHITE}  {END}'
    BLACKBOX = '  '
    for i in range(min(start_a, start_b), diagram_height):
        print(f'{i*len(list)/diagram_height:.2f}', end='  ')
        if i >= start_a:
            print(WHITEBOX, end='  ')
        else:
            print(BLACKBOX, end='  ')
        if i >= start_b:
            print(WHITEBOX)
        else:
            print(BLACKBOX)