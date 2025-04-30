# Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña.
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Crea un objeto usando la clase.
user1 = User('Tiana', 'test1234')

print(user1.username)
print(user1.password)
