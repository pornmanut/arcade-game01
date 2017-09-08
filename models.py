import arcade.key
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.ship = Ship(self,width/2,height/6)


    def update(self, delta):
        self.ship.update(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.ship.DIRECTION = 1
        if key == arcade.key.DOWN:
            self.ship.DIRECTION = 3
        if key == arcade.key.LEFT:
            self.ship.DIRECTION = 0
        if key == arcade.key.RIGHT:
            self.ship.DIRECTION = 2

class Ship:
    DIRECTION = 1
    #0 left
    #1 up
    #2 right
    #3 down
    SPEED = 3

    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

    def switch_direction(self):
        if(self.DIRECTION == 0):
            self.angle = 90
        elif(self.DIRECTION == 1):
            self.angle = 0
        elif(self.DIRECTION == 2):
            self.angle = -90
        else:
            self.angle = 180

    def update(self,delta):
        self.switch_direction()
        if(self.DIRECTION):
            if(self.y > self.world.height):
                self.y = 0
            self.y += Ship.SPEED
        else:
            if(self.x > self.world.width):
                self.x = 0
            self.x += Ship.SPEED
