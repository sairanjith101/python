from unicodedata import name
from xml.dom.pulldom import CHARACTERS


class book:

    name = 'House of the Dragon'
    arthur = 'Ryan Condal George'

    def __init__(self,dragon):
        self.drogen = dragon

    def characters (self,Rhaenyra_Targaryen,Daemon_Targaryen):
        self.mainrole = Rhaenyra_Targaryen
        self.villanrole = Daemon_Targaryen
        print(Rhaenyra_Targaryen,Daemon_Targaryen)

object = book('Srax')
print(object.name)
print(object.arthur)
print(object.drogen)
object.characters('King of Targaryens','peerless warrior')