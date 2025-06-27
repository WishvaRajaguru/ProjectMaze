from __future__ import annotations
from abc import ABC,abstractmethod
from enum import Enum

class Block(ABC):
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def compare(self, block: Block): # x and y are not equal to passed states coordinates
        raise Exception("Block compare is not supported")

class State(Block):
    def compare(self, block: State):
        return block.x is self._x and block.y is self._y

class Wall(Block):
    def compare(self, block: Wall):
        return block.x is self._x and block.y is self._y

class Path(Block):
    def compare(self, block: Path):
        return block.x is self._x and block.y is self._y

class Step(Block):
    def compare(self, block: Path):
        return block.x is self._x and block.y is self._y

class Start(Block):
    def compare(self, block: Start):
        return block.x is self._x and block.y is self._y

class Goal(Block):
    def compare(self, block: Goal):
        return block.x is self._x and block.y is self._y

class Action(Enum):
    UP = "UP" # y - 1
    DOWN = "DOWN" # y + 1
    LEFT = "LEFT" # x - 1
    RIGHT = "RIGHT" # x + 1

class Node:
    def __init__(self, state: State, parent: Node = None, action: Action = None):
        self.state = state  # State that represents the node
        self.parent = parent  # The State before this
        self.action = action  # The action applied to the parent to become current state


class Frontier(ABC):
    def __init__(self):
        self._frontier: list[Node] = [] # the frontier that contains identified future states
        self._explored: list[Node] = [] # the list of Nodes that are already explored

    def add(self, node:Node): # add a node to frontier (if not it is in the frontier and explored lists)
        if not self.contains_state(node.state):
            self._frontier.append(node)

    def contains_state(self, state):
        return any(node.state.compare(state) for node in self._frontier) or any(node.state.compare(state) for node in self._explored)

    def empty(self):
        return len(self._frontier) == 0

    @abstractmethod
    def pop(self) -> Node:
        pass

    def len(self):
        return len(self._frontier)

    def remove(self, node: Node):
        self._frontier.remove(node)
        self._explored.append(node)


# Last in first out
class StackFrontier(Frontier):
    def pop(self) -> Node:
        if self.empty():
            raise Exception("The frontier stack is empty")
        else:
            node = self._frontier.pop()
            self._explored.append(node)
            return node


# First in first out
class QueueFrontier(Frontier):
    def pop(self) -> Node:
        if self.empty():
            raise Exception("The frontier queue is empty")
        else:
            node = self._frontier.pop(0)
            self._explored.append(node)
            return node

