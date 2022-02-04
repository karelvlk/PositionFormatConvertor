
from formats.BaseFormat import BaseFormat

class XMLformat(BaseFormat):
    def __init__(self, data):
        super().__init__(data)
        self.inputPath = data[0]
        self.outputPath = data[1]
        self.format = data[2]
        self.delimiter = data[3]
        self.skipHeader = data[4]

    def generateStart(self):
        self.startLines.append('<?xml version="1.0" encoding="UTF-8"?>')
        self.startLines.append('<points>')

    def generateEnd(self):
        self.endLines.append('</points>')

    def convertLines(self):
        if self.skipHeader == 'A':
            j = 1
        else:
            j = 0

        for i in range (j, len(self.lines)):
            line = self.lines[i]

            line = line.replace('\n', '').split(self.delimiter)
            self.convertedLines.append(f'<point>')
            self.convertedLines.append('<coords>')
            self.convertedLines.append(f'<x>{line[2]}</x>')
            self.convertedLines.append(f'<y>{line[3]}</y>')
            self.convertedLines.append(f'<z>{line[4]}</z>')
            self.convertedLines.append('</coords>')
            self.convertedLines.append('<properties>')
            self.convertedLines.append(f'<name>{line[0]}</name>')
            self.convertedLines.append(f'<dummy>{line[1]}</dummy>')
            self.convertedLines.append(f'<omega>{line[5]}</omega>')
            self.convertedLines.append(f'<phi>{line[6]}</phi>')
            self.convertedLines.append(f'<kappa>{line[7]}</kappa>')
            self.convertedLines.append('</properties>')
            self.convertedLines.append(f'</point>')