from logger import*

def interface():
    try:
        # comment:
        cmd = ""
        while cmd != 5:
            print("Выберите вариант действия: \n"\
                "1.Создать заметку\n"\
                "2.Удалить заметку \n"\
                "3.Показать заметки\n"\
                "4.Изменить заметки\n"\
                "5.Выход"  )
            cmd = input("Введите номер операции: ")
            if cmd < 1 or cmd > 5:
                raise ValueError("Введите целое числовое значение из списка")
            if cmd == "1":
                input_data()
            elif cmd == "2":
                delite_note()
            elif cmd == "3":
                readmy_note()
            elif cmd == "4":
                replace_note()
            print("Всего доброго") 
    except TypeError as e:
        print("Возникла ошибка!")
    # end try
    
        