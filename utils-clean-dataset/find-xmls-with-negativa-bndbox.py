import os
import argparse
from lxml import etree

def find_negative_bndbox_values(directory):
    # Recorre todos los archivos en el directorio
    for filename in os.listdir(directory):
        if filename.endswith('.xml'):
            file_path = os.path.join(directory, filename)
            tree = etree.parse(file_path)
            root = tree.getroot()
            
            # Busca todos los elementos <object>
            objects = root.findall('.//object')
            
            for obj in objects:
                bndbox = obj.find('bndbox')
                if bndbox is not None:
                    try:
                        xmin = int(bndbox.find('xmin').text)
                        ymin = int(bndbox.find('ymin').text)
                        xmax = int(bndbox.find('xmax').text)
                        ymax = int(bndbox.find('ymax').text)
                    except Exception as e:
                        print(e)
                        print(filename)
                        exit(0)
                    
                    if xmin <= 0 or ymin <= 0 or xmax <= 0 or ymax <= 0:
                        print(f"Archivo '{filename}' contiene un <bndbox> con valores negativos: "
                              f"xmin={xmin}, ymin={ymin}, xmax={xmax}, ymax={ymax}")
                        break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encuentra archivos XML con valores de bndbox negativos.")
    parser.add_argument("directory", type=str, help="Ruta al directorio con los archivos XML")
    args = parser.parse_args()
    
    find_negative_bndbox_values(args.directory)

