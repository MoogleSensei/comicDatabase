# Data Reader
# A simple csv to dict/list function.
# It will take a csv and create this python object,
# comics, as a list of entries from the generated dict.
import csv

def getComics():
    comics = []
    inputFile = csv.DictReader(open("comics.csv"))
    for row in inputFile:
        comics.append(row)
    return comics
    