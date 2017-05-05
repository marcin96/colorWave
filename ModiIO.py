import xml.etree.ElementTree as ET
from xml.dom import minidom
import Modus
import tag as tg
import Breakpoint


def prettify(element):
    rough_string = ET.tostring(element, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def read_Modus(ModNode):
    '''
    '''
    ret = Modus.Modus(ModNode.get("name"))
    ret.Benutzer = ModNode.find("Benutzer").text
    ret.erstelltam = ModNode.find("erstelltAm").text
    ret.veraendertam = ModNode.find("verandertAm").text
    ret.Beschreibung = ModNode.find("Beschreibung").text
    ret.intervall = ModNode.find("Interval").text
    ret.wechsel = ModNode.find("wechselfluessig").text
    tags = []
    for tag in ModNode.find("Tags"):
        tags.append(tg.Tag(tag.text))
    ret.tags = tags
    Breakpoints = []
    for point in ModNode.find("Breakpoints"):
        tmp = Breakpoint.Breakpoint(int(point.get("Farbtemperatur")),int(point.get("Zeit")))
        tmp.Beschreibung = point.find("Beschreibung").text
        Breakpoints.append(tmp)
    ret.breakpoints=Breakpoints
    return ret

def update_Modus(root,tree,path,Mode):
    '''
    '''
    try:
        remove_Modus(Mode.name,root,tree,path)
    except:
        None
    add_Modus(Mode,root)
    save_Modis(tree,path)

def remove_Modus(Modi_name,root,tree,path):
    '''
    '''
    toRem = None
    print(Modi_name)
    for elem in root:
        if(elem.get("name").strip() == Modi_name.strip()):
            print(Modi_name,elem.get("name").strip())
            toRem = elem
            break
    if(toRem!=None):root.remove(toRem)
    save_Modis(tree,path)

def add_Modus(Modus,root):
    '''
    '''
    ModNode = ET.Element("Modus")
    ModNode.set("name",Modus.name)
    Benutzer = ET.Element("Benutzer")
    Benutzer.text = "heyMann"
    erstelltAm = ET.Element("erstelltAm")
    erstelltAm.text = str(Modus.erstelltam)
    verandertAm = ET.Element("verandertAm")
    verandertAm.text= str(Modus.veraendertam)
    Beschreibung = ET.Element("Beschreibung")
    Beschreibung.text= str(Modus.Beschreibung)
    Intervall = ET.Element("Interval")
    Intervall.text=str(Modus.intervall)
    Wechsel = ET.Element("wechselfluessig")
    Wechsel.text= str(Modus.wechsel)
    ModNode.append(Benutzer)
    ModNode.append(erstelltAm)
    ModNode.append(verandertAm)
    ModNode.append(Beschreibung)
    ModNode.append(Intervall)
    ModNode.append(Wechsel)
    Tags = ET.Element("Tags")
    for tag in Modus.tags:
        tagEL = ET.Element("Tag")
        tagEL.text = tag.name
        Tags.append(tagEL)
    ModNode.append(Tags)
    Breakpoints = ET.Element("Breakpoints")
    for point in Modus.breakpoints:
        pointEL = ET.Element("Breakpoint",{"Farbtemperatur":str(point.Farbtemperatur),"Zeit":str(point.Zeit)})
        Breakpoints.append(pointEL)
        bp = ET.Element("Beschreibung")
        bp.text=str(point.Beschreibung)
        pointEL.append(bp)
    ModNode.append(Breakpoints)
    root.append(ModNode)
    
def save_Modis(tree,name):
    '''
    '''
    tree.write(name)

def readXML(xml):
    tree = ET.parse(xml)
    root = tree.getroot()
    return (root,tree)


def readModis(root):
    '''
    '''
    Modi = []
    for modus in root.findall('Modus'):
        Modi.append(read_Modus(modus))
    return Modi

#root,tree = readXML("Modi.xml")
#modis = readModis(root)
#print(len(modis))
'''tmp = Modus.Modus("Temp Modus")
tmp.Benutzer="chee"
tmp.erstelltam="22"
tmp.veraenderam="33"
tmp.intervall="30"
tmp.wechsel="True"
tmp.tags= ["Arbeit","Auto"]
b = Breakpoint.Breakpoint(2000,9)
b.Beschreibung="Sonnenaufgang"
tmp.breakpoints.append(b)
tmp.breakpoints.append(Breakpoint.Breakpoint(3000,12))
tmp.breakpoints.append(Breakpoint.Breakpoint(5000,14))
tmp.breakpoints.append(Breakpoint.Breakpoint(2000,18))
add_Modus(tmp,root)
save_Modis(tree,"Modi.xml")'''

