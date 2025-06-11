from xml.dom import minidom as xml


waren_dict = {}
xmldoc = xml.parse("waren.xml")

waren = xmldoc.getElementsByTagName("waren")[0]
artikel = waren.getElementsByTagName("artikel")

for a in artikel:
    nr = int(a.getElementsByTagName("nr")[0].firstChild.data)
    bezstr = a.getElementsByTagName("bez")[0].firstChild.data
    vol = float(a.getElementsByTagName("volumen")[0].firstChild.data)
    preis = float(a.getElementsByTagName("preis")[0].firstChild.data)
    print(nr, bezstr, vol, preis)
    waren_dict[nr] = [bezstr, vol, preis]


root = xml.Document()
preise = root.createElement("preise")
root.appendChild(preise)

for artikel in waren_dict:
    artikelpreis_node = root.createElement("artikelpreis")
    artikelpreis_node.setAttribute("preisart", "literpreis")
    nr_node = root.createElement("nr")
    textnode = root.createTextNode(str(artikel))
    nr_node.appendChild(textnode)
    bez_node = root.createElement("bez")
    textnode = root.createTextNode(waren_dict[artikel][0])
    bez_node.appendChild(textnode)
    preis_node = root.createElement("preis")
    textnode = root.createTextNode(
        str(round(waren_dict[artikel][2] / waren_dict[artikel][1], 2))
    )
    preis_node.appendChild(textnode)
    artikelpreis_node.appendChild(nr_node)
    artikelpreis_node.appendChild(bez_node)
    artikelpreis_node.appendChild(preis_node)
    preise.appendChild(artikelpreis_node)

xml_str = root.toprettyxml(indent="\t")
f = open("preise.xml", "wt")
f.write(xml_str)
f.close()
