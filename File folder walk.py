import os

# Set the directory you want to start from
rootDir = r'\\...\\...\\Docs'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Directory: %s' % dirName.replace(rootDir,''))
    for fname in fileList:
        print('\t%s' % fname)

print('done')