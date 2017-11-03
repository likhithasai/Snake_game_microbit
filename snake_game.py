from microbit import *
import random
import music

class Snake:
    """ This class contains the functions that operate
        on our game as well as the state of the game.
        It's a handy way to link the two.
        """

    def __init__(self):
        """ Special function that runs when you create
            a "Snake", ie. when you run
            game = Snake()
            init stands for "Initialisation"
            """
        ## current direction is a string with up, down, left or right
        self.current_direction = "down"
        ## snake is a list of the pixels that the snake is at
        self.snake = [[3,1]]
        ## food is the co-ords of the current food
        self.food = [1, 1]
        self.count = 0
        ## whether or no to end the game, used after update
        self.end = False
        pass

    def handle_input(self):
        """ We'll use this function to take input from the
            user to control which direction the snake is going
            in.
            """

        if abs(accelerometer.get_x) > abs(accelerometer.get_y):
            if accelerometer.get_x > 0:
                self.current_direction = "right"
            elif accelerometer.get_x < 0:
                self.current_direction = "left"
        elif abs(accelerometer.get_x) < abs(accelerometer.get_y):
            if accelerometer.get_y > 0:
                self.current_direction = "down"
            elif accelerometer.get_y < 0:
                self.current_direction = "up"
        pass

    def update(self):
        """ This function will update the game state
            based on the direction the snake is going.
            """
        # The line below makes a copy of the head of the snake
        # you will be working with that copy in this function
        new_head = list(self.snake[-1])
        if self.current_direction == "up":
            new_head[1] = new_head[1] - 1
            if new_head[1] < 0:
                new_head[1] = 4
        elif self.current_direction == "down":
            new_head[1] = new_head[1] + 1
            if new_head[1] > 4:
                new_head[1] = 0
        elif self.current_direction == "right":
            new_head[0] = new_head[0] + 1
            if new_head[0] > 4:
                new_head[0] = 0
        else:
            new_head[0] = new_head[0] - 1
            if new_head[0] < 0:
                new_head[0] = 4
        if new_head == self.food:
            self.food[0] = int(random.randint(0, 4))
            self.food[1] = int(random.randint(0, 4))
            self.count = self.count + 1
            if new_head in self.snake:
                self.end = True
            self.snake.append(new_head)
        else:
            if new_head in self.snake:
                self.end = True
            self.snake.append(new_head)
            self.snake = self.snake[1:]
        pass

    def draw(self):
        """ This makes the game appear on the LEDs. """
        display.clear()
        display.set_pixel(self.food[0], self.food[1], 9)
        for part in self.snake:
            display.set_pixel(part[0], part[1], 7)

# game is an "instance" of Snake
game = Snake()

# this is called our "game loop" and is where everything
# happens
while True:
    game.handle_input()
    sleep(1000)
    game.update()
    if game.end == True:
        game.count = str(game.count)
        display.scroll(game.count)
        break
    game.draw()
    # this makes our micro:bit do nothing for 500ms
    sleep(500)
