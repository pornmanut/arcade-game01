import arcade.key

from random import randint
class Model:
    def __init__(self,world,x,y,angle=None):
        self.world = world
        self.x = x
        self.y = y
        if(angle != None):
            self.angle = angle
        else:
            self.angle = 0
    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.score = 0
        self.ship = Ship(self,width/2,height/6)
        self.gold = Gold(self,width/2,height/2)

    def update(self, delta):
        self.ship.update(delta)

        if self.ship.hit(self.gold, 20):
            self.gold.random_location()
            self.score += 1

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.ship.DIRECTION = 1
        if key == arcade.key.DOWN:
            self.ship.DIRECTION = 3
        if key == arcade.key.LEFT:
            self.ship.DIRECTION = 0
        if key == arcade.key.RIGHT:
            self.ship.DIRECTION = 2

class Gold(Model):

    def __init__(self,world,x,y):
        super().__init__(world,x,y)
    def random_location(self):
        self.x = randint(0+1,self.world.width-1)
        self.y = randint(0+1,self.world.height-1)

class Ship(Model):
    DIRECTION = 1
    SPEED = 5

    def __init__(self,world,x,y):
        super().__init__(world,x,y)

    def move_controler(self):
        if(self.DIRECTION == 0):
            self.angle = 90
            self.x -= Ship.SPEED
        elif(self.DIRECTION == 1):
            self.angle = 0
            self.y += Ship.SPEED
        elif(self.DIRECTION == 2):
            self.angle = -90
            self.x += Ship.SPEED
        else:
            self.angle = 180
            self.y -= Ship.SPEED

    def over_edge(self):
        if(self.DIRECTION == 0):
            if(self.x < 0):
                self.x = self.world.width
        elif(self.DIRECTION == 1):
            if(self.y > self.world.height):
                self.y = 0
        elif(self.DIRECTION == 2):
            if(self.x > self.world.width):
                self.x = 0
        else:
            if(self.y < 0):
                self.y = self.world.height

    def update(self,delta):
        self.move_controler()
        self.over_edge()
