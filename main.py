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

"""
def extrair_info():
    print("Carregando informações fiscais dos arquivos")
    tree = ET.parse('')
    root = tree.getroot()
    print(root)
extrair_info() """