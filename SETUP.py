FIRE_WATER_BOOL = False # should fire/water be used for true/false instead of vitae

REPEATS_PER_CASE = 4 # how many times to add atom in a single case
CASES_TO_ADD = 8 # how many cases to calculate
BLOCK_REPEAT_CASES = True # if test cases can have duplicates
CASE_LENGTH = REPEATS_PER_CASE
OUTPUT_NAME = "Output"
OUTPUT_DESC = "Invert Fire in the input to Water, and vice-versa. The Salt is to show which end is the start."
INPUT_NAME = "Input"
INPUT_DESC = "A line of 4 atoms of Fire or Water, randomly chosen, with Salt at the start."

PUZZLE_ID = "invert" # puzzle idea here

CATALYST_IDS = ["fire", "water"] # the list of atoms to make catalysts for
# you must directly supply the atom ID, we cant import ATOMS since ATOMS is importing here

ATOM_PREFIX = "salt"
ATOM_APPEND = "none" #atoms to put at start/end, none means nothing