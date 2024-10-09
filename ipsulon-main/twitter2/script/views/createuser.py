from script.services.windows import *
from script.services.bankedit import *
from script.models.user import *
from script.database.usersDb import *
from script.services.windows import App

class Createuser(Window):
    def __init__(self, master: App, name: str='create'):
        super().__init__(master, name)
        self.grid_rowconfigure(0, weight=6)
        self.grid_columnconfigure(0, weight=1)
        fontfamily = 'arial'
        title = (fontfamily,20,'bold')
        description=(fontfamily,15,'bold')
        self.welcomelabel = Text(self,text='BEM VINDO AO ÍPSULON',font=title)
        self.descriptlabel = Text(self,text='Criar Perfil',font=description)
        self.entrynick = Entry(self,'Nickname')
        self.entryuser = Entry(self,'username')
        self.entrypass = Entry(self,'senha')
        self.logbutton = Button(self,text='criar',command=self.createuser)

        self.add_element(self.welcomelabel,row=0,column=0)
        self.add_element(self.descriptlabel,row=1,column=0)
        self.add_element(self.entryuser,row=2,column=0)
        self.add_element(self.entrypass,row=3,column=0)
        self.add_element(self.entrynick,row=4,column=0)
        self.add_element(self.logbutton,row=5,column=0)
    
    def createuser(self):
        username = self.entryuser.get()
        password = self.entrypass.get()
        nickname = self.entrynick.get()

        userdb = UserDatabase()
        userdb.add_user(username,password,nickname)

        self.master.change_window('login')