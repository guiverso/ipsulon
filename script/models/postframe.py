from typing import Any, Tuple
from script.services.windows import *

class PostFrame(Frame):
    def __init__(self, master: Any,nickname,content,username, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str] = "transparent", fg_color: str | Tuple[str] | None = None, border_color: str | Tuple[str] | None = None, background_corner_colors: Tuple[str | Tuple[str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        fontfamily = 'arial'
        fontname = (fontfamily,14,'bold')
        fontcontent = (fontfamily,12)
        self.window = self.master.master.master.master
        
        self.nickname = Button(self,text=nickname,font=fontname,fg_color='transparent',command=self.to_profile)
        self.content = Text(self,wraplength=400,text=content,font=fontcontent)
        self.edit = Button(self,text='editar')
        self.delete = Button(self,text='deletar')

        self.add_element(self.nickname,expandTo='w')
        self.add_element(self.content,row=1)

        if self.window.master.user == username:
            self.add_element(self.edit,row=0,column=1)
            self.add_element(self.delete,row=1,column=1)
    
    def to_profile(self):
        return self.window.to_profile()