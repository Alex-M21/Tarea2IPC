import xml.dom.minidom

document = xml.dom.minidom.parse("librery.xml")
#ES UN OBJETO
mapping = {}
#REFERENCIA PARA EL OBJETO

for nodeBook in document.getElementsByTagName("book"):
#ITERA LA ETIQUETA BOOK DENTRO DEL XML
    isbn = nodeBook.getAttribute("isbn")
    #OBTENEMOS EL ATRIBUTO ISBN DENTRO DEL XML
    titles = nodeBook.getElementsByTagName("title")
    #OBTENEMOS LOS ELEMENTOS DEL TITULO DENTRO DEL XML

    for nodeTitle in titles:
    # OBTENEMOS CADA TIPPO DE ELEMENTO  
        nodeText = nodeTitle.firstChild
        title = nodeText.data
        mapping[isbn]=title
print(mapping)
