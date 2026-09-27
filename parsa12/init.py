playlist={}
class Add:
    def __init__(self,singer,trach):
        self.singer=singer
        self.trach=trach
    def __str__(self):
        playlist[self.singer]=[self.trach]
        return f"{self.singer},{self.trach}"
class remove:
    def __init__(self,singer,music):
        self.singer=singer
        self.music=music
    def __str__(self):
        playlist[self.singer].remove(self.music)
        return f" in trach:{self.music} hazf shode."
        
    

user1=Add("pishro","divone")
user2=Add("pishro","HSHA")
user3=remove("pishro","divone")
print(user1,user2)
print(playlist)
