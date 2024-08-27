import sqlite3

def create_connection():
    return sqlite3.connect('login.db')

def define_cursor(conexao):
    return conexao.cursor()

def create_table(conexao, cursor):

    cursor.execute('''

        CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL
        );
    
    ''')

def main():
    conexao = create_connection()
    cursor = define_cursor(conexao)
    create_table(conexao, cursor)

if __name__ == '__main__':
    main()