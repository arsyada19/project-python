from direct.showbase.ShowBase import ShowBase

#from mapmanager import Mapmanager

from mapmanager import Mapmanager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand(r"C:\Users\anisa\Documents\panda3d_land\panda3d_land") 
        base.camLens.setFov(120)

game = Game()
game.run()  

