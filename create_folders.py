"""
-------------------------------------------------------------------------------
 Creates the following project structure within the current working
 directory:
   .
   ├── 01-code-scripts
   ├── 02-raw-data
   ├── 03-processed-data
   ├── 04-graphics-outputs
   └── 05-papers-writings
-------------------------------------------------------------------------------
 Author:  Cale Kochenour
 Contact: cale.kochenour@alumni.psu.edu
 License: MIT
-------------------------------------------------------------------------------
"""
# -------------------------ENVIRONMENT SETUP--------------------------------- #
# Import packages and modules
import os

# -------------------------DATA PREPROCESSING-------------------------------- #
# Create folders
for folder in [
    "01-code-scripts",
    "02-raw-data",
    "03-processed-data",
    "04-graphics-outputs",
    "05-papers-writings",
]:
    if os.path.exists(folder):
        print(f"'{folder}' already exists. Skipped.")
    else:
        os.mkdir(folder)
        print(f"Created '{folder}'")

# -------------------------SCRIPT COMPLETION--------------------------------- #
print("\n")
print("-" * (18 + len(os.path.basename(__file__))))
print(f"Completed script: {os.path.basename(__file__)}")
print("-" * (18 + len(os.path.basename(__file__))))
print("\n")
