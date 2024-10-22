from script.services.windows import *
from script.services.builder import *
from customtkinter import set_appearance_mode

from script.database.Postsdb import *
from script.database.usersDb import *
from script.database.followdb import *

from script.models.follow import *
from script.models.posts import *
from script.models.follow import *

from script.views.login import *
from script.views.createuser import *
from script.views.feed import *
from script.views.profile import *

class Ipsulon(App):
    def __init__(self, title: str='ipsulon', geometry: str='600x600', resizable: bool = False, icon=None):
        super().__init__(title, geometry, resizable, icon)
        self.iconbitmap('script\\images\\ipsulonicon.ico')
        set_appearance_mode('dark')

        self.user = None
        self.userlist = []
        self.followerlist = []
        for user in UserDatabase().get_from("Users"):
            usermodel = User(user[0],user[1],user[2])
            self.userlist.append(usermodel) 

        for follower in FollowDatabase().get_from('Follow'):
            self.followerlist.append(Follow(follower[0],follower[1]))

        self.add_window(Login(self))
        self.add_window(Createuser(self))
        
        self.mainloop()

app = Ipsulon()