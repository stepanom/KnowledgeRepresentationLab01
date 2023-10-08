import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from agents import *

class Thing:

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property.setter
    def


class Pickup(Thing):
    pass
class Delivery(Thing):
    pass