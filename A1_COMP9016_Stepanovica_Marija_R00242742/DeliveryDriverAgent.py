import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from Thing import (Pickup, Delivery)

Void = None

class Agent:
    def isAlive(self) -> bool:
        """Things that are 'alive' should return true."""
        return hasattr(self, 'alive') and self.alive

class DeliveryDriver(Agent):
    def move(self, canMoveToSpecifiedLocation: bool = True) -> Void:
        if not canMoveToSpecifiedLocation:
            return Void
        self.direction = self.direction + d

    @staticmethod
    def deliverOrder(thing):
        if isinstance(thing, Pickup):
            return True
        return False

    @staticmethod
    def pickUpOrder(thing):
        if isinstance(thing, Delivery):
            return True
        return False