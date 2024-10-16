from script.services.bankedit import *

class UserDatabase(Database):
    def __init__(self, dbname:str='ipsulon', password: str='pabd', user: str = 'postgres', port: str = '5432', host: str = 'localhost'):
        super().__init__(dbname, password, user, port, host)
        self.usernamecollumn = Column('username','varchar',20)
        self.passwordcollumn = Column('passwrd','varchar',20)
        self.nicknamecollumn = Column('nickname','varchar',20)

        self.usernamepk = Constraint('username_pk','PRIMARY',self.usernamecollumn)

        self.create_user_table()
        
    
    def create_user_table(self):
        self.create_table('Users',(self.usernamecollumn,self.passwordcollumn,self.nicknamecollumn,self.usernamepk))

    def add_user(self,username,password,nickname):
        self.insert_in('Users',(f"'{username}'",f"'{password}'",f"'{nickname}'"))

    def get_user_by_username(self,add_user:str):
        user = self.get_from('Users',Where=True,atrsearch='username',value=f"'{add_user}'")
        return user[0]