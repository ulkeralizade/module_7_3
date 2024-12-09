def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')

    for номер_строки, строка in enumerate(strings, start=1):
        позиция_байта = file.tell()
        file.write(строка + '\n')
        strings_positions[(номер_строки, позиция_байта)] = строка
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)