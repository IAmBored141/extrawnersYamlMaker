import SETUP
import ATOMS
import WRITE_FILE
import random

atomsPool = [ATOMS.FIRE,ATOMS.WATER] # put valid atoms here
cases = [] # do not touch
results = [] # do not touch

def Computation(Atom): # type the code here
    if Atom == ATOMS.FIRE:
        return ATOMS.EARTH
    else:
        return ATOMS.AIR

print("Time to compute!")
for i in range(SETUP.CASES_TO_ADD):
    currentCaseCalculated = False
    while not currentCaseCalculated:
        tryCase = []
        tryResult = []
        for j in range(SETUP.REPEATS_PER_CASE):
            tryAtom = random.choice(atomsPool)
            tryCase.append(tryAtom)
            tryResult.append(Computation(tryAtom))
        tryCase = ATOMS.TO_ID(tryCase)
        tryResult = ATOMS.TO_ID(tryResult)
        if tryCase in cases and SETUP.BLOCK_REPEAT_CASES:
            pass # it's already there
        else:
            tryCase.insert(SETUP.ATOM_PREFIX, 0)
            tryCase.append(SETUP.ATOM_APPEND, 0)
            tryResult.insert(SETUP.ATOM_PREFIX, 0)
            tryResult.append(SETUP.ATOM_APPEND, 0)
            cases.append(tryCase)
            results.append(tryResult)
            currentCaseCalculated = True

print(cases)
print(results)
WRITE_FILE.DO(cases,results)