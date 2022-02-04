
import os
import sys
sys.path.append('formats')

from JSONformat import JSONformat
from XMLformat import XMLformat
from YAMLformat import YAMLformat
from GEOJSONformat import GEOJSONformat

def checkDataValues(outputFormats, inputFilePath, outputFilePath, outputFormat, delimiter, skipheader):
    if not os.path.exists(inputFilePath):
        print('ERROR cesta k vstupnímu souboru není validní')
        return False

    if not os.path.exists(outputFilePath):
        print('ERROR cesta k uložení konvertovaného souboru není validní')
        return False

    if not outputFormat in outputFormats:
        print('ERROR formát výsledného souboru není validní nebo není podporován')
        return False

    if delimiter == '':
        delimiter = ' '

    if skipheader == '' or skipheader != 'A':
        skipheader = 'N'

    return [inputFilePath, outputFilePath, outputFormat, delimiter, skipheader]

def checkInputData(outputFormats, inputFilePath, outputFilePath, outputFormat, delimiter, skipheader):
    if not inputFilePath or not outputFilePath or not outputFormat:
        print('+-------------------------------+')
        print('|  Vítejte v konvertoru pozic   |')
        print('+-------------------------------+')
        if not inputFilePath:
            inputFilePath = input('Zadej cestu k vstupnímu souboru: ')

        if not outputFilePath:
            outputFilePath = input('Zadej cestu k uložení konvertovaného souboru: ')

        if not outputFormat:
            outputFormat = input('Zadej formát výsledného souboru: ')

        delimiter = input('Zadej znak pro oddělovač (volinelné): ')
        skipheader = input('Je na vstupu hlavička A/N (volinelné): ')

    return checkDataValues(outputFormats, inputFilePath, outputFilePath, outputFormat, delimiter, skipheader)


def processData(data):
    if data[2] == 'GEOJSON':
        formatFile = GEOJSONformat(data)
    elif data[2] == 'JSON':
        formatFile = JSONformat(data)
    elif data[2] == 'XML':
        formatFile = XMLformat(data)
    elif data[2] == 'YAML':
        formatFile = YAMLformat(data)

    formatFile.generateStart()
    formatFile.generateEnd()
    formatFile.readLines()
    formatFile.convertLines()
    formatFile.writeConverterData()

    print('+-------------------------------+')
    print('| Konvertovaný soubor je uložen |')
    print('+-------------------------------+')

def convertToFormat(inputFilePath=None, outputFilePath=None, outputFormat=None, delimiter=' ', skipheader='N'):
    outputFormats = ['GEOJSON', 'JSON', 'XML', 'YAML']
    data = checkInputData(outputFormats, inputFilePath, outputFilePath, outputFormat, delimiter, skipheader)

    if data:
        processData(data)


convertToFormat()
