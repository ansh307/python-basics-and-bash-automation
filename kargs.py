# keyword arguments
import random
def time_activity(*arg, **kwargs):
    min = sum(arg) + random.randint(1, 60)
    choice = random.choice(list(kwargs.values()))
    print(f"Total time spent: {min} minutes on {choice}")


time_activity(10,20,30, hobby="running", sport="park", fun="football" , work="coding")