import os

def build_note(note_text, note_name):
    with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
        file.write(note_text)
    print(f"Заметка {note_name} создана.")

def create_note():
    note_name = input("Введите название заметки: ")
    note_text = input("Введите текст заметки: ")
    build_note(note_text, note_name)

def read_note(note_name):
    with open(f"{note_name}.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(f'Текст заметки: {data}\n')

def edit_note():
    ...

def delete_note():
    ...

def main():
    key = True
    while key:
        menu = {
            '1': 'create_note',
            '2': 'read_note',
            '3': 'edit_note',
            '4': 'delete_note',
        }
        for k in sorted(menu.keys()):
            print(f'{k} : {menu.get(k)}')
        
        key = input('\nВведите ключ операции, если хотите выйти, введите любые другие символы: ',)
        if key == ('1' or '2' or '3' or '4'):
            print(f'Выбрана операция: {menu[key]}\n')

        if key == '1':
            create_note()
        elif key == '2':
            note_name = input("Введите название заметки: ")
            read_note(note_name)
        elif key == '3':
            edit_note()
        elif key == '4':
            delete_note()
        else:
            key = False

    #create_note()

main()
