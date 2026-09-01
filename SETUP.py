FIRE_WATER_BOOL = False # should fire/water be used for true/false instead of vitae

REPEATS_PER_CASE = 4 # how many times to add atom in a single case
CASES_TO_ADD = 8 # how many cases to calculate
BLOCK_REPEAT_CASES = False # if test cases can have duplicates
RESULT_LENGTH_OVERRIDE = 1

COMPUTE_ENTIRE_CASE = True # whether to compute entire case at once or no

OUTPUT_NAME = "Output"
OUTPUT_DESC = "If there is an atom of Fire, return Vitae. Else, return Mors."
INPUT_NAME = "Input"
INPUT_DESC = "A line of 4 atoms of Fire or Water, randomly chosen. Water is significantly more likely to appear."

PUZZLE_ID = "detect" # puzzle ID here

CATALYST_IDS = ["fire"] # the list of atoms to make catalysts for
# you must directly supply the atom ID, we cant import ATOMS since ATOMS is importing here

# atoms to put at start/end, none means nothing
ATOM_PREFIX = "none"
ATOM_APPEND = "none"

# dont change these
RESULT_LENGTH = 0
CASE_LENGTH = REPEATS_PER_CASE