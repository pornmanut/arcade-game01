import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class snakeWindow(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height)
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

if __name__ == '__main__':
    window = snakeWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
