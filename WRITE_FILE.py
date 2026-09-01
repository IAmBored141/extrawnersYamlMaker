import SETUP
import ATOMS
import os
def DO(cases,results):
    if os.path.exists(f"output/{SETUP.PUZZLE_ID}.extrawners.yaml"):
        os.remove(f"output/{SETUP.PUZZLE_ID}.extrawners.yaml")
    with open(f"output/{SETUP.PUZZLE_ID}.extrawners.yaml", "a") as f:
        # part 1: the multi output
        f.write(f"- Type: \"MultiOutput\"\n  SinkAny: true\n  CustomName: {SETUP.OUTPUT_NAME}\n  CustomDesc: {SETUP.OUTPUT_DESC}\n  WrongMolCrashesSim: true\n  OkOutputs:\n")
        for result in results:
            f.write("    - Atoms:\n")
            for i in range(SETUP.RESULT_LENGTH):
                f.write(f"      - AtomType: {result[i]}\n")
                f.write(f"        Position:\n          Pos: {i},0\n")
            if SETUP.RESULT_LENGTH == 1:
                f.write("      Bonds: []\n")
            else:
                f.write("      Bonds:\n")
                for i in range(SETUP.RESULT_LENGTH - 1):
                    f.write(f"      - A:\n          Pos: {i},0\n")
                    f.write(f"        B:\n          Pos: {i+1},0\n")
                    f.write("        BondTypes:\n        - standard\n")
        # part 2A: the input's required outputs
        f.write(f"- Type: \"RandomInputRule\"\n  CustomName: {SETUP.INPUT_NAME}\n  CustomDesc: {SETUP.INPUT_DESC}\n  DependentOutputs:\n")
        for j in range(SETUP.CASES_TO_ADD):
            f.write("    - OutputGlyphIndex: 0\n")
            f.write(f"      OutputMoleculeIndex: {j}\n")
            f.write("      Molecules:\n")
            f.write("        - Atoms:\n")
            for i in range(SETUP.RESULT_LENGTH):
                f.write(f"          - AtomType: {results[j][i]}\n")
                f.write(f"            Position:\n              Pos: {i},0\n")
            if SETUP.RESULT_LENGTH == 1:
                f.write("          Bonds: []\n")
            else:
                f.write("          Bonds:\n")
                for i in range(SETUP.RESULT_LENGTH - 1):
                    f.write(f"          - A:\n              Pos: {i},0\n")
                    f.write(f"            B:\n              Pos: {i+1},0\n")
                    f.write("            BondTypes:\n            - standard\n")
        # part 2B: input's random options
        f.write("  RandomBag:\n")
        for case in cases:
            f.write("    - Atoms:\n")
            for i in range(SETUP.CASE_LENGTH):
                f.write(f"      - AtomType: {case[i]}\n")
                f.write(f"        Position:\n          Pos: {i},0\n")
            if SETUP.CASE_LENGTH == 1:
                f.write("      Bonds: []\n")
            else:
                f.write("      Bonds:\n")
                for i in range(SETUP.CASE_LENGTH - 1):
                    f.write(f"      - A:\n          Pos: {i},0\n")
                    f.write(f"        B:\n          Pos: {i+1},0\n")
                    f.write("        BondTypes:\n        - standard\n")
        # part 3: catalysts
        if SETUP.CASES_TO_ADD: # empty list
            for catalyst in SETUP.CATALYST_IDS:
                f.write(f"- Type: \"Spawner\"\n  CustomName: Catalyst - Elemental {catalyst.title()}\n  CustomDesc: A single atom of Elemental {catalyst.title()}.\n")
                f.write("  SpawnAtBeginning:\n")
                f.write("    - Atoms:\n")
                f.write(f"      - AtomType: {catalyst}\n")
                f.write("        Position:\n          Pos: 0,0\n")
                f.write("      Bonds: []\n")
