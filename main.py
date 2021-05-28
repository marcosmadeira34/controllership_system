from os import listdir
from os.path import isfile, join
import time
from xml.etree import ElementTree as Etree


print('Bem vindo ao leitor de arquivos XML!')
time.sleep(2.0)
print("Iniciando contagem de arquivos na pasta...")
time.sleep(3.0)

class contar_arquivos():
    def __init__(self, path, files):
        self.path = path
        self.files = files
        
path = '07_2018'
files = [f for f in listdir(path) if isfile(join(path, f))]
print(len(files),"notas fiscais localizadas...")
time.sleep(2.0)

print('Extraindo informações fiscais dos arquivos...')
time.sleep(4.0)
print('Aguarde um momento...')

# Executando parse no arquivo xml
tree = Etree.parse(r"07_2018\xml-31180722829604000188550050000405461980273977-nfe.xml")
print(Etree.tostring(tree.getroot()))


