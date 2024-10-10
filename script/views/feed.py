from script.services.windows import *
from script.services.windows import App
from script.models.user import *
from script.models.postframe import *
from script.database.Postsdb import *

class Feed(Window):
    def __init__(self, master: App, name: str = 'feed'):
        super().__init__(master, name)
        self.grid_rowconfigure(0, weight=3)
        self.grid_columnconfigure(0, weight=1)
        self.databaseposts = PostsDatabase()

        fontfamily = 'arial'
        title = (fontfamily,20,'bold')
        description=(fontfamily,15,'bold')

        self.title = Text(self,text='ÍPSULON',font=title)
        self.toprofile = Button(self,text="ir para o seu perfil",command=self.to_profile)

        self.feed = ScrollFrame(self)

        self.allposts = self.databaseposts.get_all_posts()

        for index,post in enumerate(self.allposts):
            self.feed.add_element(PostFrame(self.feed,post[1],post[2]),row=index)

        self.entryframe = Frame(self)
        self.entryframe.columnconfigure(0,weight=1)
        self.entrypost = Entry(self.entryframe,'post',limitChar=280,justify='left')
        self.sendbutton = Button(self.entryframe,text='postar',command=self.send_post)
        self.entryframe.add_element(self.entrypost,column=0)
        self.entryframe.add_element(self.sendbutton,column=1)

        self.add_element(self.title,row=0,column=0)
        self.add_element(self.toprofile, row=1)
        self.add_element(self.feed,row=2,column=0)
        self.add_element(self.entryframe,row=3,column=0)

    def send_post(self):
        username = self.master.user.username
        nickname = self.master.user.nickname
        content = self.entrypost.get()

        self.databaseposts.add_post(username,nickname,content)
        self.allposts.append([username,nickname,content])

        self.feed.add_element(PostFrame(self.feed,nickname,content,username),row=len(self.allposts))
        self.entrypost.delete(0,len(self.entrypost.get()))
    
    def to_profile(self):
        username = self.master.user.username
        return self.master.change_window(f'profile{username}')

