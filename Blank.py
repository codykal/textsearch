import glob
import sys


name=input('Please input text you would like to find: ')
sys.stdout = open(input('Please input a name for the file: ') + '.txt', "w", encoding ="utf-8", errors='replace')
#Replace Path with wherever your text file is located.
path = "D:/Collection/**/*.txt"
for filename in glob.glob('D:/Collection/**/*.txt', recursive=True):
    with open(filename, 'r', encoding="utf-8", errors='replace') as currentFile:
        text = currentFile.read()
        if (name in text):
            print(str(name + " FOUND IT " + filename))
        else:
            pass