class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.ship = Ship(self,width/2,height/6)


    def update(self, delta):
        self.ship.update(delta)

class Ship:
    Speed = 3
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
    def update(self,delta):
        if(self.y) > self.world.height :
            self.y = 0
        self.y += Ship.Speed
