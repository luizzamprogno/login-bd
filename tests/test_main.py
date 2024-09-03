import bcrypt

senha = 'senha_segura'.encode('utf-8')
salt = bcrypt.gensalt()
hash_senha = bcrypt.hashpw(senha, salt)


