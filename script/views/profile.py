from script.services.windows import *
from script.database.Postsdb import *
from script.models.postframe import *
from script.database.followdb import *

class Profile(Window):
    def __init__(self, master,ownl:bool,usersearch:str = "", name = 'profile'):
        super().__init__(master, name)
        self.rowconfigure(0,weight=4-int(ownl))
        self.columnconfigure(0,weight=1)

        self.followdb = FollowDatabase()
        self.atualusername = self.master.user.username

        fontfamily = 'arial'
        fontname = (fontfamily,24,'bold')

        self.homebtn = Button(self,text='feed',command=self.to_feed)
        self.columnconfigure(0,weight=1)
        self.usersearch = usersearch
        self.labnickname = Text(self,text=self.usersearch.nickname,font=fontname)
        self.username = Text(self,text=self.usersearch.username)
        self.followbutton = Button(self,text='seguir',command=self.follow_clbk)
        self.followedbutton = Button(self,text='seguindo',command=self.unfollow_clbk)

        self.frameposts = ScrollFrame(self)
        self.frameposts.columnconfigure(0,weight=1)

        postdb = PostsDatabase()

        allposts = postdb.get_from('Posts',Where=True,atrsearch='username',value=f"'{self.usersearch.username}'")

        for index,posts in enumerate(allposts):
            self.frameposts.add_element(PostFrame(self.frameposts,posts[2],posts[1],posts[3],posts[0],self.ownl),index)
        
        self.add_element(self.homebtn,row=0,expandTo='w')
        self.add_element(self.labnickname,row=1,expandTo='w')
        self.add_element(self.username,row=2,expandTo='w')

        if ownl == False:
            test = self.follow_check()
            if test: 
                self.add_element(self.followedbutton,row=3,expandTo='w')
                print('seguindo')
            else: 
                self.add_element(self.followbutton,row=3,expandTo='w')
                print("não está seguindo")

        self.add_element(self.frameposts,row=4-int(ownl))
    
    def to_profile(self,username):

        return self.master.change_window(f'profile{username}')
    
    def to_feed(self):
        '''feed = self.master.get_window('feed')
        feed.refresh()'''
        return self.master.change_window('feed')
    
    def follow_clbk(self):
        self.followdb.add_follower(self.usersearch.username,self.atualusername)
        self.add_element(self.followedbutton,row=3,expandTo='w')
        self.followbutton.grid_forget()
    
    def unfollow_clbk(self):
        self.followdb.delete_folower(f"'{self.usersearch.username}'",f"'{self.atualusername}'")
        self.add_element(self.followbutton,row=3,expandTo='w')
        self.followedbutton.grid_forget()

    def follow_check(self):
        for follow in self.followdb.get_from('Follow',Where=True,atrsearch='follower',value=f"'{self.usersearch.username}'"):
            if follow[0] == self.atualusername:
                return True
            else:
                return False