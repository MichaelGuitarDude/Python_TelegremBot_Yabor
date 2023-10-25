from os import remove
from os.path import isfile

def build_note(note_text, note_name):
    with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
        file.write(note_text)
    print(f"Заметка {note_name} создана.")

def create_note():
    note_name = input("Введите название заметки: ")
    note_text = input("Введите текст заметки: ")
    build_note(note_text, note_name)

def read_note():
    ...

def edit_note():
    ...

def delete_note():
    ...

def main():
    ...

main()
