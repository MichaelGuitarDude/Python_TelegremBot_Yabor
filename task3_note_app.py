import os
from colorama import init, Fore, Style
init(autoreset=True)



def build_note(note_text, note_name):
    with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
        file.write(note_text)
    print(Style.BRIGHT + Fore.GREEN + f"Заметка {note_name} создана.")


def create_note(note_name):
    note_text = input("Введите текст заметки: ")
    build_note(note_text, note_name)


def read_note(note_name):
    if os.path.isfile(f"{note_name}.txt"):
        with open(f"{note_name}.txt", "r", encoding="utf-8") as file:
            note_text = file.read()
        print(Style.BRIGHT + Fore.GREEN + f'Текст заметки: {note_text}')
    else: 
        print(Fore.RED + 'Заметка не найдена.')


def edit_note(note_name):
    if os.path.isfile(f"{note_name}.txt"):

        # Читаем файл и выводим на экран
        with open(f"{note_name}.txt", "r", encoding="utf-8") as file:
            note_text = file.read()
        print(Style.BRIGHT + Fore.BLUE + f'Старый текст заметки: {note_text}')

        # Перезаписываем файл и тоже выводим на экран
        with open(f"{note_name}.txt", "w+", encoding="utf-8") as file:
            note_text = input('Введите новый текст: ')
            file.write(note_text)
            #print(Style.BRIGHT + Fore.GREEN + f'Новый текст заметки: {file.read()}\n')
        print(Style.BRIGHT + Fore.GREEN + 'Новый', end = ' ')
        read_note(note_name)
        print(Style.BRIGHT + Fore.CYAN + 'Текст заметки успешно перезаписан.')
    else: 
        print(Fore.RED + 'Заметка не найдена.')


def delete_note(note_name):
    if os.path.isfile(f"{note_name}.txt"):
        os.remove(f"{note_name}.txt")
        print(Style.BRIGHT + Fore.RED + 'Файл удалён!')
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
        for k in sorted(menu.keys()):
            print(f'{k} : {menu.get(k)}')
        
        key = input('\nВведите ключ операции. Если хотите выйти, введите любые другие символы: ',)
        if key == '1' or key == '2' or key == '3' or key == '4':
            print(Style.BRIGHT + Fore.CYAN + f'Выбрана операция: {menu[key]}\n')
            note_name = input("Введите название заметки: ")
        else:
            print(Style.BRIGHT + Fore.CYAN + 'Работа программы завершена.\n')

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
