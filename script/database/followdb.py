from script.services.bankedit import *

class FollowDatabase(Database):
    def __init__(self, dbname='ipsulon', password='pabd', user = 'postgres', port = '5432', host = 'localhost'):
        super().__init__(dbname, password, user, port, host)
        self.coluser = Column('username','varchar',20)
        self.colfollower = Column('follower','varchar',20)

        self.constuser = Constraint('username_fk','FOREIGN',self.coluser,'Users','username',references='username')
        self.constfollow = Constraint('follower_fk','FOREIGN',self.colfollower,'Users',references='username')
        self.create_table_follow()

    def create_table_follow(self):
        return self.create_table('Follow',(self.coluser,self.colfollower,self.constuser,self.constfollow))
    
    def add_follower(self,username,follower):
        return self.insert_in('Follow',(f"'{username}'",f"'{follower}'"))
    
    def delete_folower(self,username,follower):
        return self.delete('Follow',True,condition=f"username = '{username}' AND follower = '{follower}'")