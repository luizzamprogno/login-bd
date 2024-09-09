# Sistema de Login com SQLite

Este projeto implementa um sistema de login simples utilizando o prórpio terminal e um banco de dados SQLite para armazenar os dados dos usuários.

## Funcionalidades

- Registro de novos usuários
- Login de usuários com verificação de credenciais
- Senhas armazenadas de forma segura utilizando hashing
- Mensagens de erro e sucesso exibidas no terminal

## Tecnologias Utilizadas

- [Python](https://www.python.org/) - Linguagem de programação
- [SQLite3](https://www.sqlite.org/index.html) - Banco de dados leve e integrado
- [bcrypt](https://pypi.org/project/bcrypt/) - Biblioteca para hash de senhas

## Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

## Como Usar

1. **Configuração Inicial:**
    - O banco de dados será criado automaticamente na primeira execução do projeto.
    - O banco de dados estará no arquivo `cadasdtro.db` no diretório raiz.

2. **Executar para interagir com o terminal:**

    ```bash
    python src/main.py
    ```

3. **Registro de Novo Usuário:**
    - Escolha a opção 1 do menu.
    - Insira um nome de usuário e uma senha e clique ENTER no teclado.

4. **Login:**
    - Escolha a opção 2 no menu.
    - Insira o nome de usuário e a senha e clique no botão clique ENTER no teclado.
    - Mensagens de erro aparecerão se o usuário não existir ou se as credenciais forem inválidas.

## Estrutura do Projeto

```plaintext
login-bd/
│
├── src/
│   ├── database.py     # Código relacionado ao banco de dados
│   └── main.py         # Arquivo principal que inicializa a aplicação
│
└── README.md           # Documentação do projeto