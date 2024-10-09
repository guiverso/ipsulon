from script.services.windows import *

class Profile(Window):
    def __init__(self, master, name = 'profile'):
        super().__init__(master, name)
        self.labnickname = Text(self,text='nickname')
        self.username = Text(self,text='username')

        self.frameposts = ScrollFrame(self)