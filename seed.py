# Code for anything to do with the seed, seed generating, seed reading and controll


import random as rd
from tracemalloc import start

# Generate seed
def generate():
    l = str(rd.randint(5,50))
    l = l.zfill(2)
    h = str(rd.randint(2,50))
    h = h.zfill(2)
    z = str(rd.randint(1,5))
    unique_identifier = str(rd.randint(0,99999))
    unique_identifier = unique_identifier.zfill(5)
    return l + h + z + unique_identifier

    #return str(rd.randint(0,50)) + str(rd.randint(0,50)) + str(rd.randint(0,5)) + str(rd.randint(0,99999))

def read(strg):
    l = int(strg[:2])
    h = int(strg[2:4])
    z = int(strg[4])
    unique_identifier = int(strg[5:])
    return (l,h,z, unique_identifier)

def sum_1(strg):
    sum = 0
    for i in strg[:3]:
        sum += int(i)
    return sum

def sum_2(strg):
    sum = 0
    for i in strg[3:]:
        sum += int(i)
    return sum

def start_and_end(coords:tuple):
    if coords[3] % 4 == 0: #na vrhu, na desni
        starting_x, starting_y = coords[0] // sum_1(str(coords[3])), 0
        ending_x, ending_y = coords[0], coords[1] // sum_2(str(coords[3]))
    elif coords[3] % 4 == 1: #na levi, na desni
        starting_x, starting_y = 0, coords[1] // sum_1(str(coords[3]))
        ending_x, ending_y = coords[0], coords[1] // sum_2(str(coords[3]))
    elif coords[3] % 4 == 2: #na vrhu, na podnu
        starting_x, starting_y = coords[0] // sum_1(str(coords[3])), 0
        ending_x, ending_y = coords[0] // sum_2(str(coords[3])),coords[1]
    elif coords[3] % 4 == 3: #na levi, na podnu
        starting_x, starting_y = 0, coords[1] // sum_1(str(coords[3]))
        ending_x, ending_y = coords[0] // sum_2(str(coords[3])), coords[1]
    return starting_x,starting_y,ending_x,ending_y



def lcg(modulus: int, a: int, c: int, seed: int):
    while True:
        seed = (a * seed + c) % modulus
        yield seed

def num_rec_lcg(seed:int):
    return lcg(2 ** 32, 1664525,1013904223, seed)

def virt_pascal_lcg(seed:int):
    return lcg( 2 ** 32, 134775813, 1, seed)

#test_lcg1 = lcg(2 ** 32,1664525,1013904223,int(generate())) #testing lcg type NUMERICAL RECIPIES at https://en.wikipedia.org/wiki/Numerical_Recipes
#test_lcg2 = lcg(2 ** 32, 134775813, 1, int(generate())) at https://en.wikipedia.org/wiki/Virtual_Pascal
#print([next(test_lcg1) for i in range(20)])
#print([next(test_lcg2) for i in range(20)])


# basic_map = 0,0

# def steps(map:tuple , starting_l=0, starting_h=1,):
#     map_length = sum(int(i) for i in str(map[3])) #<----- calculate map length based on unique_identifier
#     list_of_steps = []
#     i = 0
#     j = 0
#     while i <= map_length:
#         if j % 3 == 0:
#             list_of_steps.append([j % 3, (starting_l + i,starting_h), 0])
#             i += 2
#             j += 1
#         elif j % 3 == 1:
#             list_of_steps.append([j % 3, (starting_l + i,starting_h), 0])
#             i += 2
#             j += 1
#         elif j % 3 == 2:
#             list_of_steps.append([j % 3, (starting_l + i,starting_h - 1), 0]) 
#             i += 3
#             j += 1
#     return list_of_steps

# def basic_steps(map:tuple ,sq_side:int, starting_x=0, starting_y=0,):
#     map_length = sum(int(i) for i in str(map[3]))
#     list_of_steps = []
#     i = 0
#     while i <= map_length:
#         list_of_steps.append([i % 3, (starting_x + 2 * i * sq_side, starting_y), 0])
#         i += 1
#     return list_of_steps

class map:
    def __init__(self,seed:str):
        """turn this thing into a dataclass-"""
        self.seed = seed
        self.dimensions = read(self.seed)
        self.x = self.dimensions[0]
        self.y = self.dimensions[1]
        self.complexity = self.dimensions[2]
        self.unique_identifier = str(self.dimensions[3])
        self.length = self.x + self.y -2
        for i in self.unique_identifier:
            self.length += int(i)
        self. length = self.length * self.complexity
        self.lcg = num_rec_lcg(int(self.seed))
        self.lcg_list = [next(self.lcg) for _ in range(self.length)]
        self.start_x, self.start_y, self.end_x, self.end_y = start_and_end(self.dimensions)
        self.starting_coords = self.start_x, self.start_y
        self.finish_coords = self.end_x, self.end_y
        self.exceptions = None
        self.matrix = []


    def __repr__(self) -> str:
        return f"{self.dimensions})"

    def __str__(self) -> str:
        return f"steps"

    def exception_library(self):
        self.exceptions = {}
        self.exceptions[self.starting_coords] = 1
        self.exceptions[self.finish_coords] = 1
        k = 2
        while k <= self.length:
            for i in range(self.y +1):
                for j in range(1,self.x +1):
                    if (j-1,i) in self.exceptions:
                        self.exceptions[(j,i)] = 1
                        k += 1
                    elif (j,i-1) in self.exceptions:
                        self.exceptions[(j,i)] = 1
                        k += 1
                    else:
                        continue
        #This fucker right here can fuck right the fuck off fuckin g piece of shit fuck shit
        return self.exceptions

    def grid_matrix(self):
        matrix = []
        for i in range(self.y+1):
            row = []
            for j in range(self.x+1):
                if (j,i) in self.exceptions:
                    row.append(self.exceptions[(j,i)])
                else:
                    row.append(0)
            print(row)
            matrix.append(row)
        self.matrix = matrix.copy()

