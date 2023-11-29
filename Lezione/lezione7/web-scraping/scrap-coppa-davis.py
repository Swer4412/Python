import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL della pagina Wikipedia
url = "https://it.wikipedia.org/wiki/Coppa_Davis"

# Effettua una richiesta HTTP alla pagina
response = requests.get(url)

# Analizza il contenuto HTML della pagina con BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Estrai la seconda tabella della pagina (indice 1)
table = soup.find_all("table", {"class": "wikitable"})[1]

# Estrai le righe della tabella
rows = table.find_all("tr")
print(rows)

# Estrai l'intestazione della tabella
header = ['Paese', 'Vittorie', 'Ultima vittoria', 'Finali perse', 'Ultima finale persa']

# Inizializza una lista per i dati della tabella
data = []

# Itera sulle righe della tabella (ignorando l'intestazione)
for row in rows[1:]:
    # Estrai le colonne della riga
    columns = row.find_all(["td", "th"])

    # Estrai i dati dalla riga e aggiungili alla lista
    row_data = [column.get_text(strip=True) for column in columns]
    print(row_data)
    data.append(row_data)

# Crea un DataFrame pandas con i dati estratti
df = pd.DataFrame(data, columns=header)
print(df)

# Rimuovi eventuali righe vuote
df = df.dropna()

# Salva il DataFrame in un file CSV
df.to_csv("coppa_davis.csv", index=False)

print("File CSV salvato con successo.")