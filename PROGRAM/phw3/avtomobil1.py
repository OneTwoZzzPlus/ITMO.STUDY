from random import random
from time import sleep
import os

time = 5
car_positions = [1, 1, 1]


def move_cars():
    global car_positions
    for i in range(len(car_positions)):
        if random() > 0.3:
            car_positions[i] += 1


def draw_cars():
    global car_positions
    for i in range(len(car_positions)):
        print('-' * car_positions[i])
    
    
while time:
    # decrease time
    time -= 1
    sleep(1)
    os.system('cls' if os.name=='nt' else 'clear')
    move_cars()
    draw_cars()
        

