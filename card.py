import suit


#
# Card is a class that holds a suit and a value.
# The values range from  2 to 14 where 11 is Jack, 12 is Queen, 13 is King and 14 is Ace
#
class Card:
    suit
    value = 0

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    def __str__(self):
        if self.value <= 10 and self.value != 1:
            return str(self.suit) + ' ' + str(self.value)

        elif self.value == 11:
            return str(self.suit) + ' J'

        elif self.value == 12:
            return str(self.suit) + ' Q'

        elif self.value == 13:
            return str(self.suit) + ' K'
        elif self.value == 14:
            return str(self.suit) + ' A'

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        if self.suit < other.suit:
            return True
        elif self.suit > other.suit:
            return False
        else:
            return self.value < other.value
