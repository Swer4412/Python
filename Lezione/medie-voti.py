import csv

# con l'apertura di file
# with è stato aggiunto perchè tutti si dimenticavano di chiudere il file (file.close())
# with lo fa in automatico
with open('./Lezione/voti.csv', 'r') as file:
  #Questa funzione crea un dizionario dal file csv, pazzurdo neh
  csv_file = csv.DictReader(file) 

  for row in csv_file:
    print(row)
#{'nome': 'Marco', 'voto1': '8', 'voto2': '7', 'voto3': '9'}
#{'nome': 'Anna', 'voto1': '10', 'voto2': '9', 'voto3': '10'}
#{'nome': 'Luca', 'voto1': '6', 'voto2': '5', 'voto3': '7'}
#{'nome': 'Sara', 'voto1': '9', 'voto2': '8', 'voto3': '8'}

  for row in csv_file:
    print(row["nome"])
