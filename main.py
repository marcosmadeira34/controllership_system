# Libries import

from os import listdir, path
from os.path import isfile, join
import time
from xml import etree
import xml.etree.ElementTree as et


list_xml = []
def captura_xml():    
    path = input("Digte o caminho do arquivo: ")
    files = [f for f in listdir(path) if isfile(join(path, f))]
    list_xml.append(files)
    print("Aguarde...")
    print(len(files),"notas fiscais localizadas...")
    time.sleep(3.0)
    directory = path    
    list_files = []
    files = [f for f in listdir(directory) if f.endswith('.xml')]
    
    for x in files:
        list_files.append(x)
    print(list_files)

    mytree = et.parse(r'')
    myroot = mytree.getroot()
    print(myroot)
    time.sleep(5.0)
    print('aguarde.....')

    for child in myroot.findall(' ide '):
        cUF = child.find('cUF').text
        cNF = child.get('cNF').text
        print(cUF, cNF)

captura_xml()

