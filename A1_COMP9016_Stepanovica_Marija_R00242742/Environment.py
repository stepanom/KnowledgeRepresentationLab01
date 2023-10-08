import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from agents import *

class Environment2D(XYEnvironment):
    def __init__(self, width = 3, height = 3):
        super().__init__(width, height)

    def percept(self, agent):
        things = self.list_things_at(agent.location)
        loc = copy.deepcopy(agent.location)  # find out the target location
        # Check if agent is about to bump into a wall
        if agent.direction == Direction.R:
            loc[0] += 1
        elif agent.direction == Direction.L:
            loc[0] -= 1
        elif agent.direction == Direction.D:
            loc[1] += 1
        elif agent.direction == Direction.U:
            loc[1] -= 1
        if not self.is_inbounds(loc):
            things.append(Boundary())
        return things

    def execute_action(self, agent, action):
        if action == 'move':

        if action == 'goRight':
            print('{} decided to {} at location: {}'.format(str(agent)[1:-1], action, agent.location))
            agent.turn(Direction.R)
        elif action == 'goLeft':
            print('{} decided to {} at location: {}'.format(str(agent)[1:-1], action, agent.location))
            agent.turn(Direction.L)
        elif action == 'goUp':
            print('{} decided to move {}wards at location: {}'.format(str(agent)[1:-1], agent.direction, agent.location))
            agent.turn(Direction.U)
        elif action == 'goDown':
            print('{} decided to move {}wards at location: {}'.format(str(agent)[1:-1], agent.direction, agent.location))
            agent.turn(Direction.D)
        elif action == "pickUpOrder":
            item = self.list_things_at(agent.location, tclass=Pickup)
            if len(item) != 0:
                if agent.pickupOrdeer(item[0]):
                    print(f"{agent} picked up {item[0]} at location {agent.location}")
                    self.delete_thing(item[0])
        elif action == "deliverOrder":
            item = self.list_things_at(agent.location, tclass=Delivery)
            if len(item) != 0:
                if agent.deliverOrder(item[0]):
                    print(f"{agent} delivered {item[0]} at location {agent.location}")
                    self.delete_thing(item[0])


    def is_done(self):

        no_orders = not any(isinstance(thing, Delivery) or isinstance(thing, Pickup) for thing in self.things)
        dead_agents = not any(agent.is_alive() for agent in self.agents)
        return no_orders or dead_agents
