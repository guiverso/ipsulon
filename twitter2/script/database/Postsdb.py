from script.services.bankedit import *

class PostsDatabase(Database):
    def __init__(self, dbname: str='ipsulon', password: str='pabd', user: str = 'postgres', port: str = '5432', host: str = 'localhost'):
        super().__init__(dbname, password, user, port, host)
        self.colnick = Column('nickname','varchar',20)
        self.colusername = Column('username','varchar',20)
        self.colcontent = Column('content','varchar',280)

        self.constusername = Constraint('username_fk','FOREIGN',atrref=self.colusername,tableref='users')
        test = self.create_table_content()
        print(test)

    def create_table_content(self):
        return self.create_table('Posts',(self.colusername,self.colnick ,self.colcontent,self.constusername))
    
    def add_post(self,username,content,likes=0):
        return self.insert_in('Posts',(f"'{username}'",f"'{content}'"))
    
    def get_all_posts(self):
        return self.getall()

