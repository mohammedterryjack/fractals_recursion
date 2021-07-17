class Recursive:
    def __init__(self, function:callable) -> None:
        self.function = function
        self.cache = {}
        self.branching_factor = 3
    
    def memoise(self, *args):
        key = '_'.join(str(arg) for arg in args)
        if key not in self.cache:
            self.cache[key] = self.function(*args)
        return self.cache[key]
    
    def __call__(self, *args):
        for _ in range(self.branching_factor):
            return self.memoise(*args)

    # if stopping_condition(value,angle):
    #     raise StopIteration
        
    # do_something(value,angle)

    # for _ in range(branching_factor):
    #     recursive_function(*update(value,angle,branching_factor))


from turtle import Screen, Turtle

environment = Screen()
agent = Turtle()

@Recursive
def flower(distance:int, angle:int):
    agent.forward(distance)
    agent.right(angle)
    return flower(distance-1, angle+1)

flower(40,10)
environment.exitonclick()

# seed_value = 50
# seed_angle = 180
# seed_branching_factor = 2

# def stopping_condition(value,angle):
#     return value <= 1

# def do_something(value,angle):
#     agent.right(angle)
#     agent.forward(value)

# def update(value, angle, branching_factor):
#     new_value = value
#     new_angle = (angle + 89)%360
#     new_branching_factor = branching_factor
#     return new_value, new_angle, new_branching_factor

# try:
#     recursive_function(seed_value,seed_angle,seed_branching_factor)
# except StopIteration:
#     pass 
