from script.services.windows import *
from customtkinter import set_appearance_mode

from script.database.Postsdb import *
from script.database.usersDb import *

from script.views.login import *
from script.views.createuser import *
from script.views.feed import *
from script.views.profile import *

PostsDatabase()
UserDatabase()

class Ipsulon(App):
    def __init__(self, title: str='ipsulon', geometry: str='600x600', resizable: bool = False, icon=None):
        super().__init__(title, geometry, resizable, icon)
        self.iconbitmap('script\\images\\ipsulonicon.ico')
        set_appearance_mode('dark')

        self.user = None
        self.userlist = []
        for user in UserDatabase().get_from("Users"):
            self.userlist.append(User(user[0],user[1],user[2]))

        self.login = Login(self)

        self.add_window(self.login)
        self.add_window(Createuser(self))
        
        self.mainloop()

Ipsulon()