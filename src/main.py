import sqlite3
import bcrypt

def create_connection():
    return sqlite3.connect('cadastro.db')

def define_cursor(conexao):
    return conexao.cursor()

def menu():
    return int(input('''
        *** MENU ***

        (1) - Create new user
        (2) - Login
        (3) - Exit

    '''))

def create_table(conexao, cursor):

    cursor.execute('''

        CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL
        );
    
    ''')

    conexao.commit()

def user_decision(conexao, cursor):

    choices = {
        1: create_new_user,
        2: login
    }

    while True:

        user_choice = menu()

        if user_choice in choices:
            choices[user_choice](conexao, cursor)
        elif user_choice == 3:
            conexao.close()
            break
        else:
            print('\nPlease, enter a valid option')

def hash_password(user_password):

    salt = bcrypt.gensalt()
    return bcrypt.hashpw(user_password.encode('utf-8'), salt)

def create_new_user(conexao, cursor):

    user = input('Enter a new user name: ')
    password = input('Chose a password: ')

    hashed_password = hash_password(password)

    db_user = check_user_existence(cursor, user)

    if db_user is None:
        cursor.execute('''

            INSERT INTO Usuarios (nome, senha)
            VALUES  (?, ?)

        ''', (user, hashed_password))

        print(f'\nUser {user} created')

        conexao.commit()
    else:
        print(f'\nUsername {user} already exists')

def check_user_existence(cursor, user):

    cursor.execute('''
        SELECT COUNT(*)
        from Usuarios
    ''')

    count = cursor.fetchone()[0]

    if count == 0:
        pass
    else:
        cursor.execute('''
            SELECT nome
            FROM Usuarios
            WHERE nome = ?

        ''', (user,))

        return cursor.fetchone()

def login(conexao, cursor):

    user = input('Usuário: ')
    password = input('Senha: ')

    try:
        cursor.execute('''
            SELECT senha 
            FROM Usuarios 
            WHERE nome = ?
        
        ''', (user,))

        result = cursor.fetchone()[0]

        if result is None:
            print(f'\nUser {user} not found')

        if verify_password(password, result):
            print(f'\nLogin succesfull')
        else:
            print(f'\nWrong password')


    except TypeError:
        print(f'\nUser {user} not Found')

def verify_password(given_password, hashed_password):

    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(given_password.encode('utf-8'), hashed_password)

def main():
    
    conexao = create_connection()
    cursor = define_cursor(conexao)
    create_table(conexao, cursor)
    user_decision(conexao, cursor)
    conexao.close()

if __name__ == '__main__':
    main()