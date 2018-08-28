from enum import Enum


class Suit(Enum):

    HEART = 'heart'
    SPADE = 'spade'
    DIAMOND = 'diamond'
    CLUB = 'club'
    NONE = 'none'

    def __lt__(self, other):
        if self == Suit.DIAMOND:
            return False
        elif self == Suit.SPADE:
            return True
        elif self == Suit.CLUB and other == Suit.SPADE:
            return False
        elif self == Suit.CLUB:
            return True
        elif self == Suit.HEART and other == Suit.DIAMOND:
            return True
        else: return False

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)