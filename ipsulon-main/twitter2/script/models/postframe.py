from typing import Any, Tuple
from script.services.windows import *

class PostFrame(Frame):
    def __init__(self, master: Any,nickname,content, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str] = "transparent", fg_color: str | Tuple[str] | None = None, border_color: str | Tuple[str] | None = None, background_corner_colors: Tuple[str | Tuple[str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        fontfamily = 'arial'
        fontname = (fontfamily,14,'bold')
        fontcontent = (fontfamily,12)
        
        self.nickname = Text(self,text=nickname,font=fontname)
        self.content = Text(self,wraplength=600,text=content,font=fontcontent)

        self.add_element(self.nickname)
        self.add_element(self.content,row=1)