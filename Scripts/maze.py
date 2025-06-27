import copy

from PIL.ImageDraw import ImageDraw

from Scripts.frontier import Node, State, Wall, Start, Goal, Step, Path, Action


class Maze:
    # the maze co-ordinates will start from top-left corner (x=0, y=0)
    def __init__(self, file: str):  # read from file and map the maze with co-ordinates
        self.__min_state: State = State(0, 0)
        self.__max_state: State = self.__min_state
        self.__start_state: State = self.__min_state
        self.__goal_state: State = self.__min_state
        self.__maze: [[]] = []
        self.__read_maze(file)

    def __read_maze(self, loc: str):
        with open(loc, "r") as file:
            y = 0
            x = 0
            maze = []
            for line in file:
                content = line.rstrip()
                maze.insert(y, [])
                for char in content:
                    if char == "#":
                        maze[y].insert(x, Wall(x, y))
                    elif char == " ":
                        maze[y].insert(x, Path(x, y))
                    elif char == "A":
                        maze[y].insert(x, Start(x, y))
                        self.__start_state = State(x, y)
                    elif char == "B":
                        maze[y].insert(x, Goal(x, y))
                        self.__goal_state = State(x, y)
                    x += 1
                self.__max_state = State(copy.copy(x), copy.copy(y))
                x = 0
                y += 1
            self.__maze = maze

    def predict_applicable_actions(self, node: Node):
        possible_nodes = list()
        for action in Action:
            possible_node = self.apply_action(node, action)
            if possible_node is not None and not self.at_wall(possible_node):
                possible_nodes.append(possible_node)
        return possible_nodes

    def apply_action(self, node: Node, action: Action) -> Node | None:
        if self.__max_state is self.__min_state or None:
            raise Exception("The maze has not been instantiated")
        else:
            if action is Action.UP and node.state.y > 0:
                return Node(State(node.state.x, node.state.y - 1), node, Action.UP)
            elif action is Action.DOWN and node.state.y < self.__max_state.y:
                return Node(State(node.state.x, node.state.y + 1), node, Action.DOWN)
            elif action is Action.LEFT and node.state.x > 0:
                return Node(State(node.state.x - 1, node.state.y), node, Action.LEFT)
            elif action is Action.RIGHT and node.state.x < self.__max_state.x:
                return Node(State(node.state.x + 1, node.state.y), node, Action.RIGHT)
            else:
                return None

    @property
    def start_state(self) -> State:
        return self.__start_state

    @property
    def goal_state(self) -> State:
        return self.__goal_state

    @property
    def max_state(self) -> State:
        return self.__max_state

    def at_goal(self, node: Node):
        if len(self.__maze) > node.state.y:
            line = self.__maze[node.state.y]
            if len(line) > node.state.x:
                char = line[node.state.x]
                return isinstance(char, Goal)
        return False

    def at_wall(self, node: Node):  # check if the passed block is a wall, true if it is
        if len(self.__maze) > node.state.y:
            line = self.__maze[node.state.y]
            if len(line) > node.state.x:
                char = line[node.state.x]
                return isinstance(char, Wall)
        return False

    def __apply_solution(self, solution: list[Node]):
        for node in solution:
            line = self.__maze[node.state.y]
            if line[node.state.x] is Wall:
                print(f"Wall in the path: {node.state.x},{node.state.y}")
            else:
                self.__maze[node.state.y][node.state.x] = Step(node.state.x, node.state.y)

    def construct_metrix(self, solution: list[Node] = None):
        if solution is not None:
            self.__apply_solution(solution)
        image = []
        for i in range(0, self.__max_state.y + 1):
            image.append([])
            line = self.__maze[i]
            for block in line:
                if isinstance(block, Start):
                    image[i].insert(block.x, "s")
                elif isinstance(block, Goal):
                    image[i].insert(block.x, "✕")
                elif isinstance(block, Wall):
                    image[i].insert(block.x, "\u2588")
                elif isinstance(block, Step):
                    image[i].insert(block.x, "●")
                else:
                    image[i].insert(block.x, " ")
        return image

    def construct_image(self, draw: ImageDraw, tile_size: int, border: int, solution: list[Node] = None):
        if solution is not None:
            self.__apply_solution(solution)
        for i in range(0, self.__max_state.y + 1):
            line = self.__maze[i]
            for block in line:
                draw.rectangle([block.x * tile_size, block.y * tile_size, block.x * tile_size + tile_size,
                                block.y * tile_size + tile_size], fill="#b7b8b6")
                if isinstance(block, Start):
                    draw.rectangle([block.x * tile_size + border, block.y * tile_size + border,
                                    block.x * tile_size + tile_size - border, block.y * tile_size + tile_size - border],
                                   fill="#a33c89")
                elif isinstance(block, Goal):
                    draw.rectangle([block.x * tile_size + border, block.y * tile_size + border,
                                    block.x * tile_size + tile_size - border, block.y * tile_size + tile_size - border],
                                   fill="#50ad2b")
                elif isinstance(block, Wall):
                    draw.rectangle([block.x * tile_size + border, block.y * tile_size + border,
                                    block.x * tile_size + tile_size - border, block.y * tile_size + tile_size - border],
                                   fill="#0e1d24")
                elif isinstance(block, Step):
                    draw.rectangle([block.x * tile_size + border, block.y * tile_size + border,
                                    block.x * tile_size + tile_size - border, block.y * tile_size + tile_size - border],
                                   fill="#9ea34d")
