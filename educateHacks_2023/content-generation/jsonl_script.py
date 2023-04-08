import csv

data = [
    ['Spanish Vocab, 2', 'Hola : Hello // Adios : Goodbye'],
    ['American Revolution, 4', 'Hola : Hello // Adios : Goodbye'],
    ['Spanish Vocab, 2', 'Hola : Hello // Adios : Goodbye'],
    ['Spanish Vocab, 2', 'Hola : Hello // Adios : Goodbye'],
    ['Spanish Vocab, 2', 'Hola : Hello // Adios : Goodbye']
]

with open('tuning_data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write multiple rows
    writer.writerows(data)