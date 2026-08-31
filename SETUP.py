FIRE_WATER_BOOL = False # should fire/water be used for true/false instead of vitae

REPEATS_PER_CASE = 4 # how many times to add atom
CASES_TO_ADD = 4 # how many cases to calculate
BLOCK_REPEAT_CASES = True # if test cases can have duplicates

OUTPUT_NAME = "Output"
OUTPUT_DESC = "Put a description here."
INPUT_NAME = "Input"
INPUT_DESC = "Put a description here."

PUZZLE_ID = "[ID]" # puzzle idea here

CATALYST_IDS = ["fire", "air", "earth"] # the list of atoms to make catalysts for
# you must directly supply the atom ID, we cant import ATOMS since ATOMS is importing here

ATOM_PREFIX = "salt"
ATOM_APPEND = "none" #atoms to put at start/end, none means nothing