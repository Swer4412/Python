from enum import Enum
from PIL import Image
from IPython.display import display
import requests
from io import BytesIO

class Suit(Enum):
    HEARTS = 'H'
    DIAMONDS = 'D'
    CLUBS = 'C'
    SPADES = 'S'

class Face(Enum):
    ACE = 'A'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '0'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'

class Card:
    PATH = "images/"

    def __init__(self, face, suit):
        if not isinstance(face, Face) or not isinstance(suit, Suit):
            raise ValueError("Invalid face or suit type.")

        self.face = face
        self.suit = suit

    #Serve per sapere il path dell'immagine su pc
    def get_image_path(self):
        #Ritorno il path della carta
        return f"{Card.PATH}{self.face.value}{self.suit.value}.png"

    #Questo mostra l'immagine
    def display_image(self):
        image = Image.open(self.get_image_path())
        display(image)

    #Scarica l'immagine
    def download_image(self):
        url = f"https://deckofcardsapi.com/static/img/{self.face.value}{self.suit.value}.png"
        print(url)
        #Faccio la richiesta all'url
        response = requests.get(url)
        #Se mi arriva una risposta positiva
        if response.status_code == 200:
            #Converto leggo i bit della risposta, e ...
            image = Image.open(BytesIO(response.content))
            image.save(self.get_image_path())
    
    def __str__(self):
        return self.get_image_path()



















