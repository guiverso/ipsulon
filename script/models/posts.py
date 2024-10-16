class Posts:
    def __init__(self,idpost,username:str,content:str,likes:int) -> None:
        self.idpost = idpost
        self.username = username
        self.content = content
        self.likes = likes