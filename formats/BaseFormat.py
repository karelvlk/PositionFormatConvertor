
import os

class BaseFormat:
    def __init__(self, data):
        self.inputPath = data[0]
        self.outputPath = data[1]
        self.format = data[2]
        self.delimiter = data[3]
        self.skipHeader = data[4]
        self.startLines = []
        self.endLines = []
        self.lines = []
        self.convertedLines = []

    def generateStart(self):
        pass

    def generateEnd(self):
        pass

    def readLines(self):
        f = open(self.inputPath, 'r')
        self.lines = f.readlines()
        f.close()

    def convertLines(self):
        pass

    def writeConverterData(self):
        head, tail = os.path.split(self.inputPath)
        tail = tail.replace('.txt', '')

        f = open(f'{self.outputPath}/{tail}.{self.format.lower()}','w+')

        for startLine in self.startLines:
            f.write(startLine)
            f.write('\n')

        for convertedLine in self.convertedLines:
            f.write(convertedLine)
            f.write('\n')

        for endLine in self.endLines:
            f.write(endLine)
            f.write('\n')

        f.close()
