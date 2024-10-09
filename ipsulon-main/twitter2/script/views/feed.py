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

        self.databaseposts.add_post('xamuel','daniel','Lorem ipsum dolor sit amet. Ad nobis eligendi qui nesciunt quae aut voluptas consequatur ut quia mollitia sed explicabo asperiores. Qui natus dicta id reiciendis sint et quisquam culpa. Quo galisum vitae est internos incidunt ad quas similique At reprehenderit voluptas aut animi')

        fontfamily = 'arial'
        title = (fontfamily,20,'bold')
        description=(fontfamily,15,'bold')

        self.title = Text(self,text='ÍPSULON',font=title)

        self.feed = ScrollFrame(self)

        allposts = self.databaseposts.get_all_posts()

        for index,post in enumerate(allposts):
            self.feed.add_element(PostFrame(self.feed,post[1],post[2]),row=index)

        print(allposts)

        self.entryframe = Frame(self)
        self.entrypost = Entry(self.entryframe,'post',limitChar=280,justify='left')
        self.sendbutton = Button(self.entryframe)
        self.entryframe.add_element(self.entrypost,column=0)
        self.entryframe.add_element(self.sendbutton,column=1)

        self.add_element(self.title,row=0,column=0)
        self.add_element(self.feed,row=1,column=0)
        self.add_element(self.entryframe,row=2,column=0)