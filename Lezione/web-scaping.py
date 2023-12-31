# Importo le librerie
import requests
from bs4 import BeautifulSoup
import pandas as pd

def main() -> None:
    # Ottengo il contenuto HTML della pagina web
    url : str = "https://en.wikipedia.org/wiki/Borg_vs_McEnroe"
    html = requests.get(url).text #Richiesta sincrona

    # Creo l'oggetto soup
    soup = BeautifulSoup(html, "html.parser")

    # Trovo la tabella che mi interessa, usando l'attributo class
    table = soup.find("table", class_="wikitable sortable")

    # Converto la tabella HTML in un DataFrame
    df = pd.read_html(str(table))[0]

    # Salvo il DataFrame in un file csv
    df.to_csv("C:\\Users\\Swer4\\Python\\Lezione\\tabella.csv", index=False, sep=";")

    print("Estrazione avvenuta con successo!")
    
if __name__ == "__main__":
    main()
