class TowerModel:
    """ Model of a Tower of Hanoi instance.
 
    Model pegs holding stacks of Disk, enforcing the constraint
    that a larger Disk may not be placed on a smaller one.
    """
 
    def __init__(self, number_of_pegs):
        """ Create new TowerModel with empty pegs
        to hold pegs of Disk.
 
        @param TowerModel self:
        @param int number_of_pegs:
        @rtype: None
 
        >>> M = TowerModel(4)
        >>> M.fill_first_peg(5)
        >>> (M.get_number_of_pegs(), M.number_of_moves()) == (4,0)
        True
        >>> M.get_number_of_disks()
        5
        """
        self._number_of_pegs = number_of_pegs
        self._pegs = []
        for i in range(number_of_pegs):
            self._pegs.append([])
        # you must have _move_seq as well as any other attributes you choose
        self._move_seq = MoveSequence([])

    def get_move_seq(self):
        """ Return the move sequence
 
        @type self: TowerModel
        @rtype: MoveSequence
 
        >>> TOH = TowerModel(2)
        >>> TOH.get_move_seq() == MoveSequence([])
        True
        """
        return self._move_seq
    
    def add(self, disk, peg_to_add_to: int) -> None:
        self._pegs[peg_to_add_to].append(disk)
    
    def fill_first_peg(self, number_of_disks) -> None:
        for i in range(number_of_disks):
            self.add(Disk(number_of_disks - i), 0)
     
    def get_top_disk(self, peg_index: int):
        if len(self._pegs[peg_index]) == 0:
            return None
        return self._pegs[peg_index][-1]
     
    def get_disk_location(self, disk) -> int:
        for peg in self._pegs:
            if disk in peg:
                return self._pegs.index(peg)
     
    def move(self, source_peg: int, target_peg: int) -> None:
        if len(self._pegs[source_peg]) == 0:
            raise IllegalMoveError
        elif len(self._pegs[target_peg]) != 0:
            if self._pegs[source_peg][-1].size >= self._pegs[target_peg][-1].size:
                raise IllegalMoveError
        self._pegs[target_peg].append(self._pegs[source_peg].pop())
        self._move_seq.add_move(source_peg, target_peg)
         
    def number_of_moves(self) -> int:
        return self._move_seq.length()
     
    def get_number_of_pegs(self) -> int:
        return len(self._pegs)
     
    def get_number_of_disks(self) -> int:
        count = 0
        for peg in self._pegs:
            count += len(peg)
        return count
 
    def __eq__(self, other):
        """ Return whether TowerModel self is equivalent to other.
 
        Two TowerModels are equivalent if their current
        configurations of disks on pegs look the same.
        More precisely, for all h,s, the h-th Disk on the s-th
        peg of self should be equivalent to the h-th Disk on the s-th
        peg of other
 
        @type self: TowerModel
        @type other: TowerModel
        @rtype: bool
 
        >>> m1 = TowerModel(4)
        >>> m1.fill_first_peg(7)
        >>> m1.move(0, 1)
        >>> m1.move(0, 2)
        >>> m1.move(1, 2)
        >>> m2 = TowerModel(4)
        >>> m2.fill_first_peg(7)
        >>> m2.move(0, 3)
        >>> m2.move(0, 2)
        >>> m2.move(3, 2)
        >>> m1 == m2
        True
        """
        if len(self._pegs) != len(other._pegs):
            return False
        for i in range(len(self._pegs)):
            if len(self._pegs[i]) != len(other._pegs[i]):
                return False
            for j in range(len(self._pegs[i])):
                if self._pegs[i][j] != other._pegs[i][j]:
                    return False
        return True
 
    def _disk_at(self, peg_index, peg_height):
        """ Return (peg_height)th from peg_index peg, if possible.
         
        @type self: TowerModel
        @type peg_index: int
        @type peg_height: int
        @rtype: disk | None
         
        >>> M = TowerModel(4)
        >>> M.fill_first_peg(5)
        >>> M._disk_at(0,3).size
        2
        >>> M._disk_at(0,0).size
        5
        """
        if 0 <= peg_height < len(self._pegs[peg_index]):
            return self._pegs[peg_index][peg_height]
        else:
            return None
 
    def __str__(self):
        """
        Depicts only the current state of the pegs and Disk.
 
        @param TowerModel self:
        @rtype: str
        """
        all_disks = []
        for height in range(self.get_number_of_disks()):
            for peg in range(self.get_number_of_pegs()):
                if self._disk_at(peg, height) is not None:
                    all_disks.append(self._disk_at(peg, height))
        max_disk_size = max([c.size for c in all_disks]) \
            if len(all_disks) > 0 else 0
        peg_str = "=" * (2 * max_disk_size + 1)
        peg_spacing = "  "
        pegs_str = (peg_str + peg_spacing) * self.get_number_of_pegs()
 
        def _disk_str(size):
            # helper for string representation of Disk
            if size == 0:
                return " " * len(peg_str)
            disk_part = "-" + "--" * (size - 1)
            space_filler = " " * int((len(peg_str) - len(disk_part)) / 2)
            return space_filler + disk_part + space_filler
 
        lines = ""
        for height in range(self.get_number_of_disks() - 1, -1, -1):
            line = ""
            for peg in range(self.get_number_of_pegs()):
                c = self._disk_at(peg, height)
                if isinstance(c, Disk):
                    s = _disk_str(int(c.size))
                else:
                    s = _disk_str(0)
                line += s + peg_spacing
            lines += line + "\n"
        lines += pegs_str
 
        return lines
 
 
class Disk:
    """ A Disk for stacking in a TowerModel
 
    === Attributes ===
    @param int size: width of Disk
    """
 
    def __init__(self, size):
        """ Initialize a disk to diameter size.
 
        @param disk self:
        @param int size:
        @rtype: None
 
        >>> c = Disk(3)
        >>> isinstance(c, Disk)
        True
        >>> c.size
        3
        """
        self.size = size
 
    def __eq__(self, other):
        """ Is self equivalent to other?
 
        We say they are if they're the same
        size.
 
        @param Disk self:
        @param Disk|Any other:
        @rtype: bool
        """
        return self.size == other.size
 
 
class IllegalMoveError(Exception):
    """ Exception indicating move that violates TowerModel
    """
    pass
 
 
class MoveSequence:
    """ Sequence of moves in TOH game
    """
 
    def __init__(self, moves):
        """ Create a new MoveSequence self.
 
        @param MoveSequence self:
        @param list[tuple[int]] moves:
        @rtype: None
        """
        # moves - a list of integer pairs, e.g. [(0,1),(0,2),(1,2)]
        self._moves = moves
 
    def __eq__(self, other):
        """ Return whether MoveSequence self is equivalent to other.
 
        @param MoveSequence self:
        @param MoveSequence|Any other:
        @rtype: bool
        """
        return type(self) == type(other) and self._moves == other._moves
         
    def get_move(self, i):
        """ Return the move at position i in self
 
        @param MoveSequence self:
        @param int i:
        @rtype: tuple[int]
 
        >>> ms = MoveSequence([(1, 2)])
        >>> ms.get_move(0) == (1, 2)
        True
        """
        if not (0 <= i < self.length()):
            raise IllegalMoveError
        return self._moves[i]
 
    def add_move(self, src_peg, dest_peg):
        """ Add move from src_peg to dest_peg to MoveSequence self.
 
        @param MoveSequence self:
        @param int src_peg:
        @param int dest_peg:
        @rtype: None
        """
        self._moves.append((src_peg, dest_peg))
 
    def length(self):
        """ Return number of moves in self.
 
        @param MoveSequence self:
        @rtype: int
 
        >>> ms = MoveSequence([(1, 2)])
        >>> ms.length()
        1
        """
        return len(self._moves)
 
    def generate_TOH_model(self, number_of_pegs, number_of_disks):
        """ Construct TowerModel from number_of_pegs and number_of_disks
         after moves in self.
 
        Takes the two parameters for
        the game (number_of_disks, number_of_pegs), initializes the game
        in the standard way with TowerModel.fill_first_peg(number_of_disks),
        and then applies each of the moves in this move sequence.
 
        @param MoveSequence self:
        @param int number_of_pegs:
        @param int number_of_disks:
        @rtype: TowerModel
 
        >>> ms = MoveSequence([])
        >>> TOH = TowerModel(2)
        >>> TOH.fill_first_peg(2)
        >>> TOH == ms.generate_TOH_model(2, 2)
        True
        """
        model = TowerModel(number_of_pegs)
        model.fill_first_peg(number_of_disks)
        for move in self._moves:
            model.move(move[0], move[1])
        return model
 
 
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)