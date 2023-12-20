from data_create import*
import os
import re
import csv 

def input_data():
    name = name_note()
    note = input_note()
    with open("note.txt", "a",encoding="utf-8") as data:
        data.write(f"{name}\n{note}\n\n")
        
def input_data_to_replace():
    return input_note()
    

def delite_note():
    delite_line = str(input("Введите название удаляемой заметки: "))
    with open("note.txt", "r",encoding="utf-8") as data:
        text = data.read()
        text_lines = text.strip().split("\n\n")
        for i, line in enumerate(text_lines):
            if delite_line in line:
                del_lines_note = line
                text_lines.pop(i)
                print(f"Удалена запись: {del_lines_note}\n")
                break
        else: print("Выбранной записи нет\n")
    with open("note.txt", 'w', newline='',encoding="utf-8") as data:
        data.write("\n\n".join(text_lines))

# def readmy_note():
#     with open("note.txt", "r",encoding="utf-8") as data:
#         text = data.read
#     print(text)
def readmy_note():
    os.system("cls")
    with open("note.txt", "r",encoding="utf-8") as data:
        print(data.read())    
    
def replace_note():
    rep_lace = str(input("Введите название изменяемой заметки: "))
    with open("note.txt", "r",encoding="utf-8") as data:
        text = data.read()
        text_lines = text.strip().split("\n\n")
        for i, line in enumerate(text_lines):
            if rep_lace in line:
                rep_note_lines = line
                print(f'Вы хотите изменить: {rep_note_lines}')
                text_lines[i] = input_data_to_replace()
    with open("note.txt", 'w', newline='',encoding="utf-8") as data:
        data.write("\n\n".join(text_lines)) 