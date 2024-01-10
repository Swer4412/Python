from itertools import product
from card import Card, Face, Suit
import random

class Deck:
    def __init__(self):
        #Product(Face, Suit) crea un insieme che contiene tutte le combinazione tra Face e Suit
        self.cards = [Card(face, suit) for face, suit in product(Face, Suit)]
    """
    def display_all_images(self):
        for card in self.cards:
            card.display_image()
    """
    def shuffle(self):
        random.shuffle(self.cards)
        
    def __str__(self):
        return ', '.join(card.get_image_path() for card in self.cards)
    
    def __iter__(self):
        self._index = 0
        return self
    
    def __next__(self):
        if self._index < len(self.cards):
            card = self.cards[self._index]
            self._index += 1
            return card
        else:
            raise StopIteration