import os
import argparse
from lxml import etree

def validate_xml_files(directory):
    # Recorre todos los archivos en el directorio
    for filename in os.listdir(directory):
        if filename.endswith('.xml'):
            file_path = os.path.join(directory, filename)
            tree = etree.parse(file_path)
            root = tree.getroot()
            
            # Busca todos los elementos <object>
            objects = root.findall('.//object')
            
            for obj in objects:
                # Verifica si el <object> contiene un <bndbox>
                if obj.find('bndbox') is None:
                    print(f"Error: El archivo '{filename}' contiene un <object> sin <bndbox>")
                    break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Valida archivos XML VOC")
    parser.add_argument("directory", type=str, help="Ruta al directorio con los archivos XML")
    args = parser.parse_args()
    
    validate_xml_files(args.directory)

