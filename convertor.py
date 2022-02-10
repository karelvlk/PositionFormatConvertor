
import os
import sys
import argparse

from formats.JSONformat import JSONformat
from formats.XMLformat import XMLformat
from formats.YAMLformat import YAMLformat
from formats.GEOJSONformat import GEOJSONformat

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
        print('| Vítejte v konvertoru formátů  |')
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
    n = formatFile.convertLines()
    formatFile.writeConverterData()

    s = ''
    m1 = ''
    m2 = ''
    for i in range (0, n+1):
        s += '-'
        if i % 2 == 0:
            m1 += ' '
        else:
            m2 += ' '

    print(f'+-------------------------------{s}+')
    print(f'|{m2} Konvertovaný soubor je uložen {m1}|')
    print(f'+-------------------------------{s}+')

def initArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')
    parser.add_argument('-f', '--format')
    parser.add_argument('-d', '--delimiter')
    parser.add_argument('-s', '--skipheader')
    return parser.parse_args()

def convertToFormat(inputFilePath, outputFilePath, outputFormat, delimiter, skipheader):
    outputFormats = ['GEOJSON', 'JSON', 'XML', 'YAML']
    data = checkInputData(outputFormats, inputFilePath, outputFilePath, outputFormat, delimiter, skipheader)

    if data:
        processData(data)

args = initArgs()
convertToFormat(args.input, args.output, args.format, args.delimiter, args.skipheader)

