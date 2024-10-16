from script.services.windows import *
from script.database.Postsdb import *
from script.models.postframe import *

class Profile(Window):
    def __init__(self, master,usersearch:str = "",ownl:bool=False, name = 'profile'):
        super().__init__(master, name)
        self.homebtn = Button(self,text='feed',command=self.to_feed)
        self.ownl = ownl
        fontfamily = 'arial'
        fontname = (fontfamily,24,'bold')
        self.columnconfigure(0,weight=1)
        self.usersearch = usersearch
        self.labnickname = Text(self,text=self.usersearch.nickname,font=fontname)
        self.username = Text(self,text=self.usersearch.username)
        self.followbutton = Checkbox(self,text='seguir')

        self.frameposts = ScrollFrame(self)
        self.frameposts.columnconfigure(0,weight=1)
        
        self.add_element(self.homebtn,row=0,expandTo='w')
        self.add_element(self.labnickname,row=1,expandTo='w')
        self.add_element(self.username,row=2,expandTo='w')
        if self.ownl == False:
            self.add_element(self.followbutton,row=3,expandTo='w')
        
        print(int(self.ownl))

        
        self.add_element(self.frameposts,row=4-int(self.ownl))

        postdb = PostsDatabase()

        allposts = postdb.get_from('Posts',Where=True,atrsearch='username',value=f"'{self.usersearch.username}'")

        for index,posts in enumerate(allposts):
            self.frameposts.add_element(PostFrame(self.frameposts,posts[2],posts[1],posts[3],posts[0],self.ownl),index)
    
    def to_profile(self,username):
        return self.master.change_window(f'profile{username}')
    
    def to_feed(self):
        return self.master.change_window('feed')
