class Card(object):
    suits = {
        'c': 'clubs',
        'd': 'diamonds',
        'h': 'hearts',
        's': 'spades'
    }
    values = {
        1: 'Ace',
        10: 'Jack',
        11: 'Queen',
        12: 'King'
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_value(self):
        return str(self.value) if self.value not in self.values else self.values[self.value]

    def get_suit(self):
        return self.suit

    def __str__(self):
        return self.get_value() + ' of ' + str(self.suit)


if __name__ == '__main__':
    my_card = Card(1, "diamonds")
    print(my_card)
