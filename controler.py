"""
Controller: User interface for manually solving
the four-pegged Tower of Hanoi puzzle.
"""

from model import TowerModel, IllegalMoveError
 
 
def move(model, origin, dest):
    """ Apply move from origin to destination in model.
 
    May raise an IllegalMoveError.
 
    @param TowerModel model:
        model to modify
    @param int origin:
        stool number (index from 0) of cheese to move
    @param int dest:
        stool number you want to move cheese to
    @rtype: None
    """
    try:
        model.move(origin, dest)
    except IllegalMoveError:
        print('\n********Illegal move, please try again********')


class ConsoleController:
    """ Controller for text console.
    """
 
    def __init__(self, disks, pegs):
        """ Initialize a new ConsoleController self.
 
        @param ConsoleController self:
        @param int disks:
        @param int pegs:
        @rtype: None
        """
        self._disks = disks
        self._pegs = pegs
 
    def play_loop(self):
        """ Play Console-based game.
 
        @param ConsoleController self:
        @rtype: None
        """

        exit = False
        tm = TowerModel(self._pegs)
        tm.fill_first_peg(self._disks)
         
        while not exit:
             
            print('*'*100)
            print(tm)
             
            inp1 = None
            valid1 = False
            while not valid1:
                try:
                    inp1 = int(input('\nEnter the peg you wish to remove the top Disk from.\nOr enter 0 if you wish to quit: '))
                    if self._pegs < inp1 or 0 > inp1:
                        raise IllegalMoveError
                    valid1 = True
                except:
                    print('\n********Invalid input, please try again.********\n')   
                    print(tm)
                     
            if inp1 == 0:
                exit = True
                print('Thank you for playing')
                break         
             
            inp2 = None
            valid2 = False
            while not valid2:
                try:
                    inp2 = int(input('\nEnter the peg you wish to move the Disk to: '))
                    if self._pegs < inp2 or 0 >= inp2:
                        raise IllegalMoveError
                    valid2 = True
                except:
                    print('\n********Invalid input, please try again.********\n')   
                    print(tm)
            move(tm, inp1-1, inp2-1)
             
            
if __name__ == '__main__':
    print('\nTower of Hanoi: At each turn select a peg to remove a Disk\n'\
    +'from, and a peg to move that Disk to. The objective is to get all the\n'\
    +'disks from the first peg to the last peg. However, you can NEVER place\n'\
    +'a larger Disk on top of a smaller Disk, so move the Disk thoughtfully.\n'\
    +'Each peg is represented by a number, where the first peg is 1, the second\n'\
    +'peg is 2, etc. Good Luck!\n\n')
     
    pegs = ''
    disks = ''
    valid1 = False
    valid2 = False
    while not valid1:
        try:
            pegs = int(input('Select the number of pegs: '))
            if pegs < 1:
                raise IllegalMoveError
            valid1 = True
        except:
            print('\nInvalid input, please try again.\n')
             
    while not valid2:
        try:
            disks = int(input('Select the number of disks: '))
            if disks < 1:
                raise IllegalMoveError
            valid2 = True
        except:
            print('\nInvalid input, please try again.\n')    
     
    console = ConsoleController(disks, pegs)
    console.play_loop()