from subprocess import PIPE, run
import os

def runELF(inFile, outFile):
    run([f"./test.elf {inFile} {outFile}"], shell=True, stdout=PIPE)

inDir = 'files'
outDir = 'decrypted'
os.mkdir(f'{outDir}')
files = os.listdir(inDir)
for i in files:
    print (f'{i}\r', end='')
    runELF(os.path.join(inDir, i), os.path.join(outDir, i))