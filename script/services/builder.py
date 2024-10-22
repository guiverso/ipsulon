from script.services.bankedit import *

from script.database.followdb import *
from script.database.usersDb import *
from script.database.Postsdb import *

class Builder:
    def __init__(self):
        self.postsdb = PostsDatabase()
        self.userdb = UserDatabase()
        self.followedb = FollowDatabase()

Builder()