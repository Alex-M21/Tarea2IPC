import xml.etree.cElementTree as ET

ruta = "C:\\Users\\braya_000\\Desktop\\XML\\" #ruta de la carpeta destino

root  = ET.Element("root")

i = 0
for numero in range(1,10):

    doc = ET.SubElement(root, "doc")
    ET.SubElement(doc,"nodo1", name="nodo").text = f"Texto nodo1 {i}"
    ET.SubElement(doc,"nodo2", atributo="manzana").text =f"Texto nodo2 {i}"

    i+=1

archivo = ET.ElementTree(root)
archivo.write(ruta+"newfile.xml")
