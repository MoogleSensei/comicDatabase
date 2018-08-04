import csv

def getComics():
    comics = []
    inputFile = csv.DictReader(open("comics.csv"))
    for row in inputFile:
        comics.append(row)
    return comics
    