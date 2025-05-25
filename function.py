'''

def add(arg1 , args2):
    return arg1 + args2

out = add(1, 2)

print(out)
print(add(1, 2))  


def adder(arg1 , args2):
    total =  arg1 + args2
    print("The total is: ", total)
    
adder(1, 2)


def sum(args):
    total = 0
    for x in args:
        total += x
    return total

out = sum([1, 2, 3, 4, 5])
print(out)

'''


# default arguments
def greetings(MSG= "morning"):
    print(f"Good {MSG}")
    
greetings()
greetings("evening") 