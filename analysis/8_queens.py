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
        if cost < best['cost'] and len(locs) == len(set(locs)):
            best = {'locations':locs, 'cost':cost}
    return best
    
def steepest_descent_optimizer(n):
    best = random_optimizer(100)
    for _ in range(n):
        best_moves = []
        for queen in range(len(best['locations'])):
            best_individual_move = []
            for transition in [(0,0),(0,1), (1,0), (0,-1), (-1,0), (1,-1), (-1,-1), (1,1), (-1,1)]:
                test_locs = [best['locations'][i] if i != queen else (best['locations'][i][0]+transition[0], best['locations'][i][1]+transition[1]) for i in range(len(best['locations']))]
                if in_bounds(test_locs) and len(test_locs) == len(set(test_locs)):
                    best_individual_move.append((test_locs,calc_cost(test_locs)))
            individual_costs = [cost for loc,cost in best_individual_move]
            best_moves.append(best_individual_move[individual_costs.index(min(individual_costs))])
        costs = [cost for loc,cost in best_moves]
        best_move = best_moves[costs.index(min(costs))]
        if best_move[1] < best['cost']:
            best = {'locations':best_move[0], 'cost':best_move[1]}
        
        
    return best

def in_bounds(locations):
    for x,y in locations:
        if x<0 or x>7 or y<0 or y>7:
            return False
    else:
        return True
            
        
        

            
for n in [10,50,100,500,1000]:
    print(n)
    result = steepest_descent_optimizer(n)
    print(result)
    #show_board(result['locations'])

