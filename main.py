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
            if SETUP.ATOM_PREFIX != "none":
                tryCase.insert(0, SETUP.ATOM_PREFIX)
                tryResult.insert(0, SETUP.ATOM_PREFIX)
                SETUP.CASE_LENGTH += 1
            if SETUP.ATOM_APPEND != "none":
                tryCase.append(SETUP.ATOM_APPEND)
                tryResult.append(SETUP.ATOM_APPEND)
                SETUP.CASE_LENGTH += 1
            cases.append(tryCase)
            results.append(tryResult)
            currentCaseCalculated = True

print(cases)
print(results)
WRITE_FILE.DO(cases,results)