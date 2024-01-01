from enum import Enum

_1st = 1
_2nd = 2
_3rd = 4
_4th = 8


class Player(Enum):
    White = 0
    Black = 1
    NONE = 2


class Cell:
    # each cell has white bitmap , black bitmap and an owner
    # cell constructor, initializes owner by none and each bitmap by zero
    def __init__(self, black_bitmap=0, white_bitmap=0):
        self.black_bitmap = black_bitmap
        self.white_bitmap = white_bitmap
        self.owner = Player.NONE

    # add gobblet returns bool if the gobblet is added, changes the bitmaps and owners
    def add_gobblet(self, player, bit):
        if self.check_validity(bit):
            if player == Player.White:
                self.white_bitmap |= bit
            elif player == Player.Black:
                self.black_bitmap |= bit
            self.change_owner()
            return True
        return False

    # remove gobblet changes owner and removes the gobblet at the top of the cell
    def remove_gobblet(self, player, bit):
        if self.owner != player:
            return False
        if player == Player.White:
            if bit > self.white_bitmap:
                return False
            self.white_bitmap &= ~bit

        elif player == Player.Black:
            if bit > self.black_bitmap:
                return False
            self.black_bitmap &= ~bit

        self.change_owner()
        return True

    # check if the gobblet can be added to this cell, by checking that the added gobblet is bigger than the cell's biggest gobblet
    def check_validity(self, bit):
        return not (self.black_bitmap >= bit or self.white_bitmap >= bit)
        
    
    # changes owner by checking the greatest bitmap
    def change_owner(self):
        if self.white_bitmap == 0 and self.black_bitmap == 0:
            self.owner = Player.NONE
        else:
            self.owner = Player.White if self.white_bitmap > self.black_bitmap else Player.Black

    # returns the owner and the biggest gobblet
    def get_gobblet(self):
        size = self.get_gobblet_size()
        return self.owner, size

    # returns the size onle
    def get_gobblet_size(self):
        if self.owner == Player.White:
            return self._get_size(self.white_bitmap)
        elif self.owner == Player.Black:
            return self._get_size(self.black_bitmap)
        return 0

    # _getsize is a helper function
    def _get_size(self, bitmap):
        if bitmap >= _4th:
            return _4th
        elif bitmap >= _3rd:
            return _3rd
        elif bitmap >= _2nd:
            return _2nd
        else:
            return _1st