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


from genericpath import isfile
from os import listdir, path
from os.path import isfile, join
import time
from xml.etree import ElementTree as ET

list_xml = []
def count_file():    
    path = input("Digte o caminho do arquivo: ")
    files = [f for f in listdir(path) if isfile(join(path, f))]
    list_xml.append(files)
    print("Aguarde...")
    #time.sleep(4)
    print(len(files),"notas fiscais localizadas...")
    time.sleep(4)
count_file()

# Executando parse no arquivo xml
def extrair_info():
    print("Carregando informações fiscais dos arquivos")
    tree = Etree.parse(r"07_2018\xml-31180722829604000188550050000405461980273977-nfe.xml")
    time.sleep(3.0)
    print("Imprimindo infomações capturadas no arquivo")
    time.sleep(2.0)
    print("....")
    print(Etree.tostring(tree.getroot()))
    root = tree.getroot()
    print("Infomações carregadas...")
    time.sleep(2.0)
    print(root)
extrair_info() 
