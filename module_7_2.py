def custom_write(file_name, strings):
    file_name1 = str(file_name)
    string1 = list(strings)
    file1 = open(file_name1, 'w', encoding='utf-8')
    strings_positions = {}
    for i in string1:
        num_string = string1.index(i)+1
        num_byte = file1.tell()
        strings_positions[(num_string, num_byte)] = str(i)
        file1.write(f'{i}\n')
    file1.close()

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

