# /// script
# dependencies = [
#   "numpy",
# ]
# ///


from pathlib import Path
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
RESOURCES_DIR = BASE_DIR.parents[2] / "resources"
DATA_DIR = BASE_DIR.parents[0] / "data"

if __name__ == "__main__":
    # Example usage of numpy dependency, can be removed
    print(np.__version__)
