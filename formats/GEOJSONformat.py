
from formats.BaseFormat import BaseFormat

class GEOJSONformat(BaseFormat):
    def __init__(self, data):
        super().__init__(data)
        self.inputPath = data[0]
        self.outputPath = data[1]
        self.format = data[2]
        self.delimiter = data[3]
        self.skipHeader = data[4]

    def generateStart(self):
        self.startLines.append('{')
        self.startLines.append('"type": "FeatureCollection",')
        self.startLines.append('"features": [')

    def generateEnd(self):
        self.endLines.append(']')
        self.endLines.append('}')

    def convertLines(self):
        if self.skipHeader == 'A':
            j = 1
        else:
            j = 0

        converted = 0
        for i in range (j, len(self.lines)):
            line = self.lines[i]
            line = line.replace('\n', '').split(self.delimiter)
            if len(line) == 8:
                converted += 1
                self.convertedLines.append('{')
                self.convertedLines.append('"type": "Feature",')
                self.convertedLines.append('"geometry": {')
                self.convertedLines.append('"type": "Point",')
                self.convertedLines.append(f'\"coordinates\": [{line[2]},{line[3]},{line[4]}]')
                self.convertedLines.append('},')
                self.convertedLines.append('"properties": {')
                self.convertedLines.append(f'\"name\": {line[0]},')
                self.convertedLines.append(f'\"dummy\": {line[0]},')
                self.convertedLines.append(f'\"omega\": {line[5]},')
                self.convertedLines.append(f'\"phi\": {line[6]},')
                self.convertedLines.append(f'\"kappa\": {line[7]}')
                self.convertedLines.append('}')
                if i == len(self.lines) - 1:
                    self.convertedLines.append('}')
                else:
                    self.convertedLines.append('},')

        n = len(str(converted)) + len(str(len(self.lines)))
        s = ''
        for i in range(0, n):
            s += '-'

        print(f'+--------------------------------{s}+')
        print(f'| Úspěšně konvertováno {converted} / {len(self.lines)-j} řádků |')
        return n

