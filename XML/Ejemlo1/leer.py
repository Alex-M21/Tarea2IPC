from xml.dom import minidom

ruta = "C:\\Users\\braya_000\\Desktop\\XML\\ejemplo.xml"
print(ruta)
xml = minidom.parse(ruta)


docs = xml.getElementsByTagName("doc")


for doc in docs:
    nodo1 = doc.getElemntsByTagName("nodo1")[0]
    nodo2 = doc.getElemntsByTagName("nodo2")[0]
    print(f"nodo1={nodo.firstChild.data} | nodo1 ={nodo.firstChild.data}")
