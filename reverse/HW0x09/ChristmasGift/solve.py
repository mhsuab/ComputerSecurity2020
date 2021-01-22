from subprocess import PIPE, run
import os

def runELF(_exeFile, _outFile, data):
    run([f"printf '{data}' |  ./{_exeFile} > {_outFile}.gz && gzip -d {_outFile}.gz"], shell=True, stdout=PIPE)
    os.chmod(_outFile, 0o775)
    if _exeFile != 'gift':
        os.remove(_exeFile)

def getInput(_exeFile):
    with open(_exeFile, 'rb') as f:
        f.seek(0xA10)
        data = f.read(256)
    return data

def getAns(exeFile):
    data = '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@terrynini@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    run([f"printf '{data}' |  ./{exeFile}"], shell=True)
    print ()

exeFile = 'gift'
i = 1

if (os.path.exists('999')):
    getAns('999')
    exit()

while True:
    if (i == 1000):
        getAns('999')
        break
    data = getInput(exeFile).decode()
    runELF(exeFile, str(i), data)
    print (data)
    exeFile = str(i)
    i += 1