FIRE_WATER_BOOL = False # should fire/water be used for true/false instead of vitae

REPEATS_PER_CASE = 6 # how many times to add atom in a single case
CASES_TO_ADD = 8 # how many cases to calculate
BLOCK_REPEAT_CASES = True # if test cases can have duplicates
RESULT_LENGTH_OVERRIDE = 1

COMPUTE_ENTIRE_CASE = True # whether to compute entire case at once or no

OUTPUT_NAME = "Output"
OUTPUT_DESC = "Count the number of Water atoms in the input, and return the metal atom with the same metallicity. As in, if there are 4 Water atoms in the input, return Copper."
INPUT_NAME = "Input"
INPUT_DESC = "A line of 6 atoms of Fire or Water, randomly chosen."

PUZZLE_ID = "count" # puzzle ID here

CATALYST_IDS = ["fire", "water"] # the list of atoms to make catalysts for
# you must directly supply the atom ID, we cant import ATOMS since ATOMS is importing here

# atoms to put at start/end, none means nothing
ATOM_PREFIX = "none"
ATOM_APPEND = "none"

# dont change these
RESULT_LENGTH = 0
CASE_LENGTH = REPEATS_PER_CASE