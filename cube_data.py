import random
import time

moves = ("U", "D", "L", "R", "F", "B")
modifiers = ("", "'", "2")

def generate_scramble(length):
    scramble = ""
    prev_move = ""
    for i in range(length):
        new_move = random.choice(moves)
        while new_move == prev_move:
            new_move = random.choice(moves)
        scramble += new_move + random.choice(modifiers) + " "
        prev_move = new_move
    return scramble[:-1]

class SolveData:

    def __init__(self, scramble, time):
        self.scramble = scramble
        self.time = time

    def __str__(self):
        return self.scramble + ": " + str(self.time)


data = []
scramble = generate_scramble(25)
ans = input(scramble + "\nPress enter to start")
while ans != "exit":
    i_time = time.perf_counter()
    input("Press enter to stop")
    f_time = time.perf_counter()
    data += [SolveData(scramble, f_time - i_time)]
    scramble = generate_scramble(25)
    ans = input(scramble + "\nPress enter to start")
for point in data:
    print(point)
