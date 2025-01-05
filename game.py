from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        x,y = self.land.loadLand(R"C:\Users\anisa\Documents\lesson3\lesson3\lesson3\land.txt")
        self.hero = Hero((30//2,30//2,2),self.land)
        base.camLens.setFov(90)

game = Game()
game.run()

