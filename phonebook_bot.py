# на 'Отлично' в одного человека надо сделать консольное приложение 
# Телефонный справочник с внешним хранилищем информации, и чтоб был реализован основной функционал:
# добавление +, просмотр+,  импорт, поиск+, удаление, изменение данных.
import sqlite3 as sq
from easygui import*

#Создание файла  *.db:

# con = sq.connect("phonebook.db")
# cur = con.cursor()
 
# cur.execute("""
# """)
 
# cur.execute("""CREATE TABLE phonebook (
#     surname TEXT,
#     name TEXT,
#     patronymic TEXT,
#     phone TEXT,
#     address TEXT
# )""")

# con.close()]

# Открырываем созданный файл:
with sq.connect("phonebook.db") as con:
    cur = con.cursor()
    cur.execute("""
    """)

cur.execute("""CREATE TABLE IF NOT EXISTS phonebook (
    surname TEXT,
    name TEXT,
    patronymic TEXT,
    phone TEXT,
    address TEXT
)""")

# Взаимодействие с программой 'Справочник' через терминал VSc:
def interface():
    var = 0
    while var != '5':
        print(
                "Варианты взаимодействия:\n"
                "1. Добавить контакт\n"
                "2. Вывести телефонную книгу в терминале\n"
                "3. Поиск контакта по параметру\n"
                "4. Выход\n"
                ) 
    
        var = input("Выберите вариант действия: ")
        while var not in ('1', '2', '3', '4', '5'):
            print("Некорректный код варианта взаимодействия")
            var = input("Выберите вариант действия: ")
        print()

        match var:
            case '1':
                add_contact() # +++
            case '2':
                show_all_phonebook() # +++
            case '3':
                seach_contact() # +++
            case '4':
                print("До свидания")
        print()

cur.execute("SELECT * FROM phonebook;")
contacts = cur.fetchall()

# Дообавление контакта в справочник:
def add_contact():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    address = input("Введите адрес(город): ")
    cur.execute("""INSERT INTO phonebook VALUES (?, ?, ?, ?, ?)""", (surname, name, patronymic, phone, address))
    con.commit()
    print()
    print("Контакт успешно добавлен!")

# Вывод телефонного справочника в терминал:
def show_all_phonebook():
    cur.execute("SELECT * FROM phonebook;")
    contacts = cur.fetchall()
    for contact in contacts:
        print(*contact)

# Поиск контакта по параметру:
def seach_contact():
    print(
        "Варианты поиска контакта:\n"
        "1. Фамилия\n"
        "2. Имя\n"
        "3. Отчество\n"
        "4. Номер телефона\n"
        "5. Адрес(город)\n")
    
    cur.execute("SELECT * FROM phonebook;")
    contacts = cur.fetchall()
    
    var = input("Выберите вариант поиска: ")
    i_var = int(var) - 2
    search = input("Введите данные для поиска: ").title()
    if search in contacts[i_var]:
                print(*contacts[i_var])
    print()

if __name__ == "__main__":
    interface()
