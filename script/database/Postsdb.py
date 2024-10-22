from script.services.bankedit import *

class PostsDatabase(Database):
    def __init__(self, dbname: str='ipsulon', password: str='pabd', user: str = 'postgres', port: str = '5432', host: str = 'localhost'):
        super().__init__(dbname, password, user, port, host)
        self.colidposts = Column('idposts','int')
        self.colnick = Column('nickname','varchar',20)
        self.colusername = Column('username','varchar',20)
        self.colcontent = Column('contents','varchar',280)

        #self.constidposts = Constraint('idposts_pk','PRIMARY')
        self.constusername = Constraint('username_fk','FOREIGN',atrref=self.colusername,tableref='Users',references='username')
        self.create_table_content()

    def create_table_content(self):
        return self.create_table('Posts',(self.colidposts,self.colusername,self.colnick ,self.colcontent,self.constusername))
    
    def add_post(self,id,username,nickname,content):
        return self.insert_in('Posts',(f"{id},'{username}'",f"'{nickname}'",f"'{content}'"))
    
    def get_all_posts(self):
        return self.get_from('Posts')

    def delete_post(self,idp):
        self.delete('Posts',where=True,condition=f"idposts = {idp}")

    def edit_post(self,idp,newvalue):
        self.edit('Posts',f"contents = '{newvalue}'",True,f'idposts = {idp}')