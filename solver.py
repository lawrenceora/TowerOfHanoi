"""
functions to run Tower of Hanoi tours.
"""

import time
from model import TowerModel


def tower_of_four_pegs(model, delay_btw_moves=0.5, animate=False):
    """Move a tower of disks from the first peg in model to the fourth.

    @type model: TowerModel
        TowerModel with tower of rings on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    @rtype: None
    """
    hanoi4(model, model.get_number_of_disks(), 0, 1, 2, 3, delay_btw_moves, animate)
    if animate:
        print(model)


def nested_i(num):
    '''Returns optimal i-value for given num of disks'''
    
    m = {1:(1,1)} #Dictionary with n-values as keys, and tuples of (minimum number of moves, corresponding i) as values'''
    
    for n in range(1,num+1):
        temp = []
        for i in range(1, n):
            value = 2*m[n-i][0] + 2**i - 1
            temp.append((value, i))
        if temp:
            m.setdefault(n, min(temp))
    return m[num][1]    


def hanoi4(model, n, start, spare1, spare2, end, time_d, animate):
    """ Solver for 4 peg tower of hanoi"""
    if n == 1:
        if animate:
            print(model)
            time.sleep(time_d)
        model.move(start, end)
    else:
        i = nested_i(n)
        hanoi4(model, n-i, start, spare2, end, spare1, time_d, animate)
        hanoi3(model, i, start, spare2, end, time_d, animate)
        hanoi4(model, n-i, spare1, start, spare2, end, time_d, animate)        


def hanoi3(model, n, start, spare, end, time_d, animate):
    """ Solver for 3 peg tower of hanoi"""
    if n == 1:
        if animate:
            print(model)
            time.sleep(time_d)
        model.move(start, end)
    else:
        hanoi3(model, n - 1, start, end, spare, time_d, animate)
        hanoi3(model, 1, start, spare, end, time_d, animate)
        hanoi3(model, n - 1, spare, start, end, time_d, animate)


if __name__ == '__main__':
    num_disks = 20
    delay_between_moves = 0.33
    console_animate = True

    four_pegs = TowerModel(4)
    four_pegs.fill_first_peg(number_of_disks=num_disks)

    tower_of_four_pegs(four_pegs,
                       animate=console_animate,
                       delay_btw_moves=delay_between_moves)

    print(four_pegs.number_of_moves())