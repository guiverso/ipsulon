from typing import Any, Tuple
from script.services.windows import *
from script.database.Postsdb import *

class PostFrame(Frame):
    def __init__(self, master: Any,nickname,username,content,id:int,ownl:bool=False, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str] = "transparent", fg_color: str | Tuple[str] | None = None, border_color: str | Tuple[str] | None = None, background_corner_colors: Tuple[str | Tuple[str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        fontfamily = 'arial'
        fontname = (fontfamily,14,'bold')
        self.username = username
        self.idpost = id
        fontcontent = (fontfamily,12)
        self.columnconfigure(0,weight=2)
        self.rowconfigure(0,weight=2)
        self.window = self.master.master.master.master
        self.database = PostsDatabase()
        
        self.nickname = Button(self,text=nickname,font=fontname,fg_color='transparent',command=self.to_profile)
        self.content = Text(self,wraplength=400,text=content,font=fontcontent)
        self.edit = Button(self,text='editar',command=self.edit_clbk)
        self.delete = Button(self,text='deletar',command=self.delete_clbk)
        self.entry = Entry(self,'novo post',limitChar=280)
        self.save = Button(self,text='salvar',command=self.save_clbk)

        self.add_element(self.nickname,expandTo='w')
        self.add_element(self.content,row=1,expandTo='w')

        if ownl:
            self.add_element(self.edit,row=0,column=1)
            self.add_element(self.delete,row=1,column=1)
    
    def to_profile(self):
        return self.window.to_profile(self.username)
    
    def delete_clbk(self):
        self.database.delete_post(self.idpost)
        
        self.destroy()

    def edit_clbk(self):
        self.add_element(self.save,row=1,column=1)
        self.add_element(self.entry,row=1,column=0)
    
    def save_clbk(self):
        newcontent = self.entry.get()

        self.database.edit_post(self.idpost,newcontent)
        self.content.configure(text=f'{newcontent}')
        self.entry.delete(0,len(self.entry.get()))

        self.save.grid_forget()
        self.entry.grid_forget()