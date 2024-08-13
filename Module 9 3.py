first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(word[0]) - len(word[1]) for word in zip(first, second) if len(word[0]) != len(word[1]))
print(list(first_result))

second_result = (len(first[index]) == len(second[index]) for index in range(len(first)))
print(list(second_result))

