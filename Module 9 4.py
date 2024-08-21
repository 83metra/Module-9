import os.path, random

print('Задание 1. Lambda-функция')
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

print('\nЗадание 2. Замыкание')

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        if os.path.isfile(f'{file_name}'):
            print(f'Файл {file_name} уже создан, перезаписываем данные:\n\t{data_set}.')
            with open(file_name, 'w+', encoding='utf-8') as file:
                for line in data_set:
                    file.write(f'{line}\n')
            print(f'Данные перезаписаны в файл: {file_name}')
        else:
            print(f'Файл {file_name} не создан, создаём его и вписываем данные:\n\t{data_set}.')
            with open(file_name, 'w',encoding='utf-8') as file:
                for line in data_set:
                    file.write(f'{line}\n')
            print(f'Данные записаны в файл: {file_name}')


    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

print('\nЗадание 3. Метод __call__')

class MysticBall:
    def __init__(self, *words):
        self.words = [word for word in words]
    def __call__(self):
        return f'Магический мяч выбирает...{random.choice(self.words)}'

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
