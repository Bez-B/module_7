import os
import time

directory = "."

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(directory, file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(os.getcwd())
        print(f'Обнаружен файл: {file}, \nПуть: {filepath}, \nРазмер: {filesize} байт, \n'
              f'Время изменения: {formatted_time}, \nРодительская директория: {parent_dir}')
