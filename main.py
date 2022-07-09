import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

play_again = True

while play_again:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    pc = Player()
    car_manager = CarManager()
    car_manager.hideturtle()
    scoreboard = Scoreboard()
    scoreboard.level_display()

    screen.onkeypress(pc.move, "w")
    screen.listen()

    gen_car = 0
    new_speed = scoreboard.current_level
    # print(new_speed)
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        gen_car += 1
        if gen_car == 6:
            car_manager.create_car()
            gen_car = 0
        car_manager.move_car(new_speed)
        for car in car_manager.all_cars:
            if car.distance(pc) < 20:
                game_is_on = False
                # scoreboard.end_game()
                another_game = screen.textinput ('GAME OVER', 'Would you like to play again?')
                if another_game == "no":
                    play_again = False
                else:
                    screen.clearscreen()
        if pc.ycor() > 280:
            scoreboard.level_display()
            pc.goto(0, -280)
            new_speed = scoreboard.current_level + 5
            # print(new_speed)
screen.bye()





