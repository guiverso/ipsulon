class User:
    def __init__(self,username,password,nickname):
        self.username = username
        self.nickname = nickname
        self.password = password

    def __str__(self):
        return f"----------------------\nApelido: {self.nickname}\nUsername: {self.username}\nSenha: {self.password}\n"