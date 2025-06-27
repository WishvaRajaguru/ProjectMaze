from PIL import Image,ImageDraw

from Scripts.maze import Maze
from Scripts.frontier import Frontier, StackFrontier, QueueFrontier, Node, State, Wall, Block

class Agent:
    def __init__(self, file: str, agl: str = "y"):
        self.__maze = Maze(file)
        self.__frontier = StackFrontier() if agl == "y" else QueueFrontier()
        self.__solutions: list[Node] = list()

    def start_process(self):
        self.__frontier.add(Node(self.__maze.start_state))

        while not self.__frontier.empty():
            # check is action applicable, check other states other than explored
            node = self.__frontier.pop()
            if self.__maze.at_goal(node):
                self.__solutions.append(node)
            else:
                possible_nodes = self.__maze.predict_applicable_actions(node)
                if len(possible_nodes) < 4:
                    for possible_node in possible_nodes:
                        self.__frontier.add(possible_node)
                else:
                    raise Exception(f"Something went wrong, there can't be {len(possible_nodes)} of possible nodes!")

        # start the solution presenting and cost calculating process
        if len(self.__solutions) == 0:
            print("No solutions were found")
        else:
            print(f"No of solutions found:  {len(self.__solutions)}")
            if len(self.__solutions) != 1:
                print("Calculating the optimal solution...")

            optimal_solution_path: list[Node] = list()
            solution_cost = 0
            for solution in self.__solutions:
                # back track each solution until the starting state
                solution_path: list[Node] = list()
                cur_cost = 0
                parent = solution.parent
                while not parent.state.compare(self.__maze.start_state):
                    solution_path.append(parent)
                    parent = parent.parent
                    cur_cost += 1

                if solution_cost < cur_cost:
                    solution_cost = cur_cost
                    optimal_solution_path = solution_path

            print(f"Total cost: {solution_cost}")
            print(f"Frontier size: {self.__frontier.len()}")
            self.print_solution(optimal_solution_path)
            img = input("Do you want the image? (y/n)")
            if img == "y":
                self.print_image(optimal_solution_path)


    def print_solution(self, solution_path: list[Node]):
        print("Preparing to print...")
        image = self.__maze.construct_metrix(solution_path)
        for line in image:
            line_str = ""
            for char in line:
                line_str += char
            print(line_str)


    def print_image(self, solution_path: list[Node]):
        tile_size = 100
        border = 2
        image = Image.new("RGB",(self.__maze.max_state.x * tile_size, (self.__maze.max_state.y + 1) * tile_size), "white")
        self.__maze.construct_image(ImageDraw.Draw(image), tile_size, border, solution_path)
        image.show()

