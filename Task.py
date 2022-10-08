import os

# вывести текущую директорию
print("Текущая деректория:", os.getcwd())

# создать пустой каталог (папку)
os.mkdir("new_folder")

# изменение текущего каталога на 'folder'
os.chdir("new_folder")

# вывод текущей папки
print("Текущая директория изменилась на new_folder:", os.getcwd())