import os
import time

directory = os.getcwd()
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = fr'{root}\{file}'
        filetime = os.stat(filepath).st_mtime
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.stat(filepath).st_size
        parent_dir = root
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
