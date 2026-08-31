import SETUP

class Atom: # just the one
    def __init__(self, atomID, value, isMetal, isCardinal):
        self.ID = atomID
        self.VALUE = value # value used for checks, normally
        self.valueType = type(value) # int, bool
        self.isMetal = isMetal
        self.isCardinal = isCardinal
    def overrideValue(self,newValue):
        self.VALUE = newValue
        self.valueType = type(newValue)
# cardinals, salt
FIRE = Atom("fire",1,False,True)
WATER = Atom("water",-1,False,True)
AIR = Atom("air",2,False,True)
EARTH = Atom("earth",-2,False,True)
SALT = Atom("salt",0,False,True)
# metals
LEAD = Atom("lead",1,True,False)
TIN = Atom("tin",2,True,False)
IRON = Atom("iron",3,True,False)
COPPER = Atom("copper",4,True,False)
SILVER = Atom("silver",5,True,False)
GOLD = Atom("gold",6,True,False)
# animismus
VITAE = Atom("vitae",True,False,False)
MORS = Atom("mors",False,False,False)

# for encoding inputs/outputs if needed
SUCCESS = GOLD
FAILURE = LEAD

def GET(value,getCardinal):
    if type(value) == bool:
        if SETUP.FIRE_WATER_BOOL: # use fire and water for booleans instead of vitae/mors
            if value:
                return FIRE
            else:
                return WATER
        else:
            if value:
                return VITAE
            else:
                return MORS
    else:
        if getCardinal:
            match value:
                case 2:
                    return AIR
                case 1:
                    return FIRE
                case 0:
                    return SALT
                case -1:
                    return WATER
                case -2:
                    return EARTH
                case _:
                    print("ERROR: desired cardinal doesnt exist")
                    return SALT
        else:
            match value:
                case 6:
                    return GOLD
                case 5:
                    return SILVER
                case 4:
                    return COPPER
                case 3:
                    return IRON
                case 2:
                    return TIN
                case 1:
                    return LEAD
                # case 0 would be Vaca
                case _:
                    print("ERROR: desired metal doesnt exist")
                    return LEAD

def TO_ID(atomList):
    outputList = []
    for atom in atomList:
        outputList.append(atom.ID)
    return outputList