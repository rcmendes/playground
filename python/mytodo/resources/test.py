import bcrypt

password = "123456"

salt = bcrypt.gensalt(10)

hash = bcrypt.hashpw(password.encode('utf8'), salt)
print(hash)
