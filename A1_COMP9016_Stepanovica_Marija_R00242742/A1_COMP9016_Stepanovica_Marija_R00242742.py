import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from agents import *
from Thing import (Pickup, Delivery)
from Environment import Environment2D

def program(percept) -> str:
    for p in percept:
        if isinstance(p, Pickup):
            return 'pickUpOrder'
        elif isinstance(p, Delivery):
            return 'deliverOrder'
        if isinstance(p, Boundary):
            turn = False
            choice = random.choice((1, 2))
        else:
            return chooseDirection()

def chooseDirection(choices: list) -> str:
    match random.choice(choices):
        case 1:
            return 'goRight'
        case 2:
            return 'goLeft'
        case 3:
            return "goUp"
        case _:
            return "goDown"

Dublin = Environment2D(color={'DeliveryDriver': (200,0,0), 'PickUp': (0, 200, 200), 'Delivery': (200, 115, 201) })
deliveryDriver = DeliveryDriver(program)
pickUp = Pickup()
delivery = Delivery()
Dublin.add_thing(deliveryDriver, [0,0])
Dublin.add_thing(pickUp, [1,2])
Dublin.add_thing(delivery, [0,1])
print(f"Random {agent} picked up the delivery and delivered it ")
Dublin.run(20)

# 0, 0 pickup -> Pickup
# 0, 0 delivery -> Delivery
# 0, 0 empty -> goRight
# 0, 0 empty -> goDown

# 0, 1 pickup -> Pickup
# 0, 1 delivery -> Delivery
# 0, 1 empty -> goRight
# 0, 1 empty -> goLeft
# 0, 1 empty -> goDown

# 0, 2 pickup -> Pickup
# 0, 2 delivery -> Delivery
# 0, 2 empty -> goLeft
# 0, 2 empty -> goDown