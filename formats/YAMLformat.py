
from formats.BaseFormat import BaseFormat

class YAMLformat(BaseFormat):
    def __init__(self, data):
        super().__init__(data)
        self.inputPath = data[0]
        self.outputPath = data[1]
        self.format = data[2]
        self.iter = data[3]
        self.skipHeader = data[4]

    def generateStart(self):
        self.startLines.append('---')
        self.convertedLines.append('points:')

    def convertLines(self):
        if self.skipHeader == 'A':
            j = 1
        else:
            j = 0

        for i in range (j, len(self.lines)):
            line = self.lines[i]
            line = line.replace('\n', '').split(self.delimiter)

            self.convertedLines.append('    - coords:')
            self.convertedLines.append(f'       x: {line[2]}')
            self.convertedLines.append(f'       y: {line[3]}')
            self.convertedLines.append(f'       z: {line[4]}')
            self.convertedLines.append('      properties:')
            self.convertedLines.append(f'       name: {line[0]}')
            self.convertedLines.append(f'       dummy: {line[1]}')
            self.convertedLines.append(f'       omega: {line[5]}')
            self.convertedLines.append(f'       phi: {line[6]}')
            self.convertedLines.append(f'       kappa: {line[7]}')