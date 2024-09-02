import sqlite3

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
            print('Please, enter a valid option')

def create_table(conexao, cursor):

    cursor.execute('''

        CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL
        );
    
    ''')

    conexao.commit()

def create_new_user(conexao, cursor):

    nome = input('Nome para cadastro: ')
    senha = input('Senha para cadastro: ')

    cursor.execute('''

        INSERT INTO Usuarios (nome, senha)
        VALUES  (?, ?)

    ''', (nome, senha))

    conexao.commit()

def login(conexao, cursor):

    user = input('Usuário: ')
    password = input('Senha: ')

    try:
        cursor.execute('''
            SELECT senha 
            FROM Usuarios 
            WHERE nome = ?
        
        ''', (user,))

        db_password = cursor.fetchone()[0]

        if db_password is None:
            return False

        if verify_password(password, db_password):
            return True
        else:
            return False

    except TypeError:
        print('User not Found')

def verify_password(given_password, db_password):

    if given_password == db_password:
        print('Login succesfull')
    else:
        print('Password doesn\'t match')

def main():
    
    conexao = create_connection()
    cursor = define_cursor(conexao)
    create_table(conexao, cursor)
    user_decision(conexao, cursor)

if __name__ == '__main__':
    main()