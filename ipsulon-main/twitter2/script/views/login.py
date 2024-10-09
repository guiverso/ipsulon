from script.services.windows import *
from script.services.bankedit import *
from script.models.user import *
from script.database.usersDb import *
from script.services.windows import App

class Login(Window):
    def __init__(self, master: App, name: str = 'login'):
        super().__init__(master, name)
        self.grid_rowconfigure(0, weight=6)
        self.grid_columnconfigure(0, weight=1)
        fontfamily = 'arial'
        title = (fontfamily,20,'bold')
        description=(fontfamily,15,'bold')
        self.welcomelabel = Text(self,text='BEM VINDO AO ÍPSULON',font=title)
        self.descriptlabel = Text(self,text='Login',font=description)
        self.entryuser = Entry(self,'username')
        self.entrypass = Entry(self,'senha')
        self.logbutton = Button(self,text='Entrar',command=self.login_callbk)
        self.creatbutton = Button(self,text='criar usuario',command=self.create_callbk)

        self.add_element(self.welcomelabel,row=0,column=0)
        self.add_element(self.descriptlabel,row=1,column=0)
        self.add_element(self.entryuser,row=2,column=0)
        self.add_element(self.entrypass,row=3,column=0)
        self.add_element(self.logbutton,row=4,column=0)
        self.add_element(self.creatbutton,row=5,column=0)
        userdb = UserDatabase()
        show = userdb.get_from('Users')
        print(show)

    def create_callbk(self):
        self.master.change_window('create')

    def login_callbk(self):
        username = self.entryuser.get()
        password = self.entrypass.get()

        userdb = UserDatabase()
        useratributs = userdb.get_user_by_username(username)
        self.user = User(useratributs[0],useratributs[1],useratributs[2])

        self.master.user = self.user

        if self.user.password == password:
            self.master.change_window('feed')
            print('senha correta!')
            print(self.master.user)
        else:
            print('senha incorreta')