import random

def show_board(locations):
    board = [[] for x in range(8)]
    all_locs = [(x,y) for x in range(8) for y in range(8)]
    for loc in all_locs:
        if loc in locations:
            board[loc[0]].append(str(locations.index(loc)))
        else:
            board[loc[0]].append('.')
    for row in board:
        print(' '.join(row))

def calc_cost(locations):
    obstructions = []
    for queen in locations:
        for elem in check_diag(queen, locations) + check_row(queen, locations) + check_columns(queen, locations):
            obstructions.append(elem)

    no_repeat = []
    for entry in obstructions:
        if entry not in no_repeat and [entry[1],entry[0]] not in no_repeat:
            no_repeat.append(entry)
    return len(no_repeat)


def check_diag(queen, locations):
    other_queens = []
    for i in range(1,8):
        if (queen[0]+i, queen[1]+i) in locations :
            other_queens.append([(queen[0]+i, queen[1]+i), queen])
        if (queen[0]-i, queen[1]-i) in locations:
            other_queens.append([(queen[0]-i, queen[1]-i), queen])
        if (queen[0]+i, queen[1]-i) in locations :
            other_queens.append([(queen[0]+i, queen[1]-i), queen])
        if (queen[0]-i, queen[1]+i) in locations :
            other_queens.append([(queen[0]-i, queen[1]+i), queen])
    return other_queens

def check_row(queen, locations):
    other_queens = []
    for loc in locations:
        if loc[0] == queen[0] and loc != queen:
            other_queens.append([loc, queen])
    return other_queens

def check_columns(queen, locations):
    other_queens = []
    for loc in locations:
        if loc[1] == queen[1] and loc != queen:
            other_queens.append([loc, queen])
    return other_queens

def random_optimizer(n):
    best = {'locations':[], 'cost': 100}
    for i in range(n):
        locs = []
        for i in range(8):
            locs.append((random.randint(0,7),random.randint(0,7)))
        cost = calc_cost(locs)
        if cost < best['cost']:
            best = {'locations':locs, 'cost':cost}
    return best
            


locations = [(0,0), (6,1), (2,2), (5,3), (4,4), (7,5), (1,6), (2,6)]
show_board(locations)
print(calc_cost(locations))
for n in [10,50,100, 500, 1000]:
    print("\nNum runs: "+str(n))
    best_result = random_optimizer(n)
    print(best_result)
