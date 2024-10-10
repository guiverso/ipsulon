from script.services.windows import *
from script.database.Postsdb import *

class Profile(Window):
    def __init__(self, master,usersearch:str = "", name = 'profile'):
        super().__init__(master, name)
        self.usersearch = usersearch
        self.labnickname = Text(self,text='nickname')
        self.username = Text(self,text='username')
        self.followbutton = Checkbox(self,text='seguir')

        self.frameposts = ScrollFrame(self)