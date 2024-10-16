from script.services.bankedit import *

class FollowDatabase(Database):
    def __init__(self, dbname='ipsulon', password='pabd', user = 'postgres', port = '5432', host = 'localhost'):
        super().__init__(dbname, password, user, port, host)
        self.coluser = Column('username','varchar',20)
        self.colfollower = Column('follower','varchar',20)

        self.constuser = Constraint('username_fk','FOREIGN',self.coluser)