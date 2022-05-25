
class Ninja:
    def __init__(self,lgen,sgen):
        self.lgen = lgen
        self.sgen = sgen
    def LeafRanks(self):
        print("Genin,Chunin,Jonin,Anbu,Hokage",self.lgen,self.sgen)
    def SandRanks(self):
        print("Genin,Chunin,Jonin,Kazekage",self.lgen,self.sgen)
leaf = Ninja('Naruto',2)

Sand = Ninja('Gaara',1)

leaf.LeafRanks()
Sand.SandRanks()
