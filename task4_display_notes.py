from os.path import isfile, splitext
from os import remove, listdir
from colorama import init, Fore, Style    # добавляем колораму, дабы текст в консоли был читабельнее
init(autoreset=True)


# Добавлена возможность чтения файлов из "блокнота" Windows (cp1251)
def encod(note_name):
    try:
        with open(f"{note_name}.txt", encoding="utf-8") as file:
            note_text = file.read()    
    except:
        with open(f"{note_name}.txt", encoding="cp1251") as file:
            note_text = file.read()
    return note_text


def build_note(note_text, note_name):
    while True:
        # Добавлена защита от перезаписи существующих файлов
        try:
            with open(f"{note_name}.txt", "x", encoding="utf-8") as file:
                file.write(note_text)
            print(Style.BRIGHT + Fore.GREEN + f"Заметка {note_name} создана.")
            break
        except:
            note_name = input('Файл уже существует! Введите название повторно: ')


# 1. Создание заметки
def create_note(note_name):
    note_text = input("Введите текст заметки: ")
    build_note(note_text, note_name)


# 2. Чтение заметки
def read_note(note_name):
    if isfile(f"{note_name}.txt"):    # проверяем, существует ли файл
        print(Style.BRIGHT + Fore.GREEN + f'Текст заметки: {encod(note_name)}')
    else: 
        print(Fore.RED + 'Заметка не найдена.')


# 3. Редактирование заметки
def edit_note(note_name):
    if isfile(f"{note_name}.txt"):  # проверяем, существует ли файл
        # Читаем файл и выводим на экран
        print(Style.BRIGHT + Fore.YELLOW + 'Старый', end = ' ')
        read_note(note_name)
        # Перезаписываем файл
        with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
            note_text = input('Введите новый текст: ')
            file.write(note_text)
        # Выводим на экран перезаписанный файл
        print(Style.BRIGHT + Fore.YELLOW + 'Новый', end = ' ')
        read_note(note_name)
        print(Style.BRIGHT + Fore.CYAN + 'Текст заметки успешно перезаписан.')
    else: 
        print(Fore.RED + 'Заметка не найдена.')


# 4. Удаление заметки
def delete_note(note_name):    
    if isfile(f"{note_name}.txt"):  # проверяем, существует ли файл
        thirst_for_deletion = input(
            "\nВы действительно хотите удалить файл?\n"
            "Если да, введите латинскую 'y', если нет - то произвольные символы: "
            )
        if thirst_for_deletion == 'y':
            remove(f"{note_name}.txt")
            print(Style.BRIGHT + Fore.RED + 'Заметка удалена!')
        else:
            print(Style.BRIGHT + Fore.CYAN + 'Удаление отменено. Возврат в Основное Меню.')    
    else: 
        print(Fore.RED + 'Заметка не найдена.')
    

# Подсчёт количества символов в файле
def file_sise(note_name):  
    return len(encod(splitext(note_name)[0]))


# 5. Вывод списка заметок
def display_notes():
    notes = [note for note in listdir() if note.endswith(".txt")]
    notes.sort(key=file_sise)    # Сортировка по длине заметок
    if notes == []:
        print(Style.BRIGHT + Fore.CYAN + 'Текстовые файлы отсутствуют.')
    else:
        notes = '\n '.join(notes)
        print(Style.BRIGHT + Fore.GREEN + '\nСписок текстовых файлов: \n', notes)



# Основной код
def main():
    while True:
        menu = {
            '1': 'create_note',
            '2': 'read_note',
            '3': 'edit_note',
            '4': 'delete_note',
            '5': 'display_notes'
        }
        print('')   # добавляем одиночный отступ
        
        # Вывод меню на экран
        for k in sorted(menu.keys()):
            print(f'{k} : {menu.get(k)}')
        
        # Выбор операции
        key = input('\nВведите ключ операции. \
Если хотите выйти, введите произвольные символы или пустоту: ').strip()

        # Вызов соответствующей операции или завершение программы        
        operation = menu.get(key)
        if None != operation != 'display_notes':    # Обработка операций с 1-ой по 4-ую
            print(Style.BRIGHT + Fore.CYAN + f'Выбрана операция: {operation}\n')
            note_name = input("Введите название заметки: ")
            globals()[operation](note_name)
        elif operation == 'display_notes':    # Обработка 5-ой операции
            display_notes()
        else:
            print(Style.BRIGHT + Fore.CYAN + 'Работа программы завершена.\n')
            break


main()
