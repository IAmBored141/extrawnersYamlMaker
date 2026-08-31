import SETUP
import ATOMS
import WRITE_FILE
import random

from SETUP import CASE_LENGTH

atomsPool = [ATOMS.FIRE,ATOMS.WATER] # put valid atoms here
cases = [] # do not touch
results = [] # do not touch

def Computation(Atom): # type the code here
    numFire = 0
    for a in Atom:
        if a == ATOMS.FIRE:
            numFire += 1
    return ATOMS.GET(numFire,False)

print("Time to compute!")
for i in range(SETUP.CASES_TO_ADD):
    currentCaseCalculated = False
    while not currentCaseCalculated:
        tryCase = []
        tryResult = []
        for j in range(SETUP.REPEATS_PER_CASE):
            tryAtom = random.choice(atomsPool)
            tryCase.append(tryAtom)
            if not SETUP.COMPUTE_ENTIRE_CASE:
                tryResult.append(Computation(tryAtom))
            elif j == (SETUP.REPEATS_PER_CASE - 1):
                tryResult.append(Computation(tryCase))
        tryCase = ATOMS.TO_ID(tryCase)
        tryResult = ATOMS.TO_ID(tryResult)
        if tryCase in cases and SETUP.BLOCK_REPEAT_CASES:
            pass # it's already there
        else:
            if SETUP.ATOM_PREFIX != "none":
                tryCase.insert(0, SETUP.ATOM_PREFIX)
                tryResult.insert(0, SETUP.ATOM_PREFIX)
            if SETUP.ATOM_APPEND != "none":
                tryCase.append(SETUP.ATOM_APPEND)
                tryResult.append(SETUP.ATOM_APPEND)
            cases.append(tryCase)
            results.append(tryResult)
            currentCaseCalculated = True
if SETUP.ATOM_PREFIX != "none":
    SETUP.CASE_LENGTH += 1
if SETUP.ATOM_APPEND != "none":
    SETUP.CASE_LENGTH += 1
if SETUP.RESULT_LENGTH_OVERRIDE != -1:
    SETUP.RESULT_LENGTH = SETUP.RESULT_LENGTH_OVERRIDE
else:
    SETUP.RESULT_LENGTH = SETUP.CASE_LENGTH

print(cases)
print(results)
print(SETUP.CASE_LENGTH)
WRITE_FILE.DO(cases,results)