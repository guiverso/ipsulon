from script.services.windows import *

from script.views.login import *
from script.views.createuser import *
from script.views.feed import *
from script.views.profile import *

class Ipsulon(App):
    def __init__(self, title: str='ipsulon', geometry: str='600x600', resizable: bool = False, icon=None):
        super().__init__(title, geometry, resizable, icon)
        self.iconbitmap('script\\images\\ipsulonicon.ico')
        self.user = None
        self.login = Login(self)

        self.add_window(self.login)
        self.add_window(Createuser(self))
        self.add_window(Feed(self))
        self.add_window(Profile(self))
        
        self.mainloop()

Ipsulon()