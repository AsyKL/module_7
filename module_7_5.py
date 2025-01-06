import os
from time import*
directory = os.getcwd()
for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(file)
    filetime = os.path.getmtime(file)
    formatted_time = strftime("%d.%m.%Y %H:%M", localtime(filetime))
    filesize = os.path.getsize(file)
    parent_dir = os.path.dirname
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

