import os
from colorama import init, Fore, Style  # добавляем колораму, дабы текст в консоли был читабельнее
init(autoreset=True)



def build_note(note_text, note_name):
    with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
        file.write(note_text)
    print(Style.BRIGHT + Fore.GREEN + f"Заметка {note_name} создана.")


def create_note(note_name):
    note_text = input("Введите текст заметки: ")
    build_note(note_text, note_name)


def read_note(note_name):
    if os.path.isfile(f"{note_name}.txt"):  # проверяем, существует ли файл
        with open(f"{note_name}.txt", "r", encoding="utf-8") as file:
            note_text = file.read()
        print(Style.BRIGHT + Fore.GREEN + f'Текст заметки: {note_text}')
    else: 
        print(Fore.RED + 'Заметка не найдена.')


def edit_note(note_name):
    if os.path.isfile(f"{note_name}.txt"):  # проверяем, существует ли файл
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


def delete_note(note_name):    
    if os.path.isfile(f"{note_name}.txt"):  # проверяем, существует ли файл
        thirst_for_deletion = input(
            "\nВы действительно хотите удалить файл?\n"
            "Если да, введите латинскую 'y', если нет - то произвольные символы: "
            )
        if thirst_for_deletion == 'y':
            os.remove(f"{note_name}.txt")
            print(Style.BRIGHT + Fore.RED + 'Файл удалён!')
        else:
            print(Style.BRIGHT + Fore.CYAN + 'Удаление отменено. Возврат в Основное Меню.')    
    else: 
        print(Fore.RED + 'Заметка не найдена.')
    


def main():
    key = True
    while key:
        menu = {
            '1': 'create_note',
            '2': 'read_note',
            '3': 'edit_note',
            '4': 'delete_note',
        }
        print('')   # добавляем одиночный отступ
        
        # Вывод меню
        for k in sorted(menu.keys()):
            print(f'{k} : {menu.get(k)}')
        
        key = input('\nВведите ключ операции. Если хотите выйти, введите произвольные символы: ')
        if key == '1' or key == '2' or key == '3' or key == '4':
            print(Style.BRIGHT + Fore.CYAN + f'Выбрана операция: {menu[key]}\n')
            note_name = input("Введите название заметки: ")
        else:
            print(Style.BRIGHT + Fore.CYAN + 'Работа программы завершена.\n')

        # Вызов соответствующей операции или завершение программы
        if key == '1':
            create_note(note_name)
        elif key == '2':
            read_note(note_name)
        elif key == '3':
            edit_note(note_name)
        elif key == '4':
            delete_note(note_name)
        else:
            key = False


main()
