def custom_write(file_name, strings):
    file = open('file_name.txt', 'w', encoding='utf-8')
    strings_positions = {}
    n = 1
    for i in strings:
        n_c = file.tell()
        strings_positions[(n, n_c)] = i
        n += 1
        file.write(i+'\n')
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