def recursive_function(value,angle,branching_factor:int):
    if stopping_condition(value,angle):
        raise StopIteration
        
    do_something(value,angle)

    for _ in range(branching_factor):
        recursive_function(*update(value,angle,branching_factor))


from turtle import Screen, Turtle

environment = Screen()
agent = Turtle()

seed_value = 50
seed_angle = 180
seed_branching_factor = 2

def stopping_condition(value,angle):
    return value <= 1

def do_something(value,angle):
    agent.right(angle)
    agent.forward(value)

def update(value, angle, branching_factor):
    new_value = value
    new_angle = (angle + 89)%360
    new_branching_factor = branching_factor
    return new_value, new_angle, new_branching_factor

try:
    recursive_function(seed_value,seed_angle,seed_branching_factor)
except StopIteration:
    pass 
