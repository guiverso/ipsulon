from script.services.windows import *
from script.database.Postsdb import *
from script.models.postframe import *

class Profile(Window):
    def __init__(self, master,usersearch:str = "", name = 'profile'):
        super().__init__(master, name)
        self.columnconfigure(0,weight=1)
        self.usersearch = usersearch
        self.labnickname = Text(self,text=self.usersearch.nickname)
        self.username = Text(self,text=self.usersearch.username)
        self.followbutton = Checkbox(self,text='seguir')

        self.frameposts = ScrollFrame(self)

        self.add_element(self.labnickname,expandTo='w')
        self.add_element(self.username,row=1)
        self.add_element(self.followbutton,row=2,expandTo='w')
        self.add_element(self.frameposts,row=3)

        postdb = PostsDatabase()

        allposts = postdb.get_from('Posts',Where=True,atrsearch='username',value=f"'{self.usersearch.username}'")

        for index,posts in enumerate(allposts):
            self.frameposts.add_element(PostFrame(self.frameposts,posts[1],posts[2],True))
